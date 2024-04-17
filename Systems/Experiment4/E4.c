#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h> 

#define BUFFER_SIZE 10

char* buffer[BUFFER_SIZE];
int in = 0;
int out = 0;


// Struct to hold producer and consumer IDs
typedef struct {
    int producer_id;
    int consumer_id;
} ThreadArgs;


// gets a random operator and returns it
char* random_operator()
{
    char* operators[] = {"+", "-", "*", "/"};
    int random_index = rand() % 4;
    char* operator = (char*)malloc(sizeof(char) * 2); 
    strcpy(operator, operators[random_index]); 
    return operator;
}


// Generate a random equation and return it
char* random_equation()
{
    int a = rand() % 100 + 1; // +1 so we done have to deal with dividing by zero
    int b = rand() % 100 + 1;
    char* operator = random_operator();
    char* equation = (char*)malloc(sizeof(char) * 10);
    sprintf(equation, "%d %s %d", a, operator, b);
    return equation;
}


// get a random equation, put it in the buffer, and print it
void* producer(void* arg)
{
    ThreadArgs* args = (ThreadArgs*)arg;
    char* equation = random_equation();
    buffer[in] = equation;
    in = (in + 1) % BUFFER_SIZE;
    printf("Producer %d ->  %s", args->producer_id, equation);
    free(args);
}


// Function does the solving and returns the result as an array of three integers
int* solve_equation(char* equation)
{
    int* result = (int*)malloc(sizeof(int) * 3);
    sscanf(equation, "%d %s %d", &result[0], (char*)&result[1], &result[2]);
    if (*(char*)&result[1] == '+')
        result[0] += result[2];
    else if (*(char*)&result[1] == '-')
        result[0] -= result[2];
    else if (*(char*)&result[1] == '*')
        result[0] *= result[2];
    else if (*(char*)&result[1] == '/')
        result[0] /= result[2];
    return result;
}


// get the equation from the buffer, solve it, and print the result
void* consumer(void* arg)
{
    ThreadArgs* args = (ThreadArgs*)arg;
    char* equation = buffer[out];
    int* result = solve_equation(equation);
    printf(" = %d  -> Consumed by %d\n", result[0], args->consumer_id);
    out = (out + 1) % BUFFER_SIZE;
    free(result);
    free(args);
}


/* 
** Run the producer-consumer setup 20 times
** Create producer and consumer threads with their respective IDs
** Wait for the producer and consumer threads to finish 
*/
int main()
{
    for (int i = 0; i < 20; i++)
    {
        int producer_id = (i % 2) + 1;
        int consumer_id = ((i / 2) % 2) + 1;
        
        pthread_t producer_thread;
        pthread_t consumer_thread;

        ThreadArgs* producer_args = (ThreadArgs*)malloc(sizeof(ThreadArgs));
        producer_args->producer_id = producer_id;
        pthread_create(&producer_thread, NULL, producer, (void*)producer_args);

        ThreadArgs* consumer_args = (ThreadArgs*)malloc(sizeof(ThreadArgs));
        consumer_args->consumer_id = consumer_id;
        pthread_create(&consumer_thread, NULL, consumer, (void*)consumer_args);

        pthread_join(producer_thread, NULL);
        pthread_join(consumer_thread, NULL);
    }

    return 0;
}
