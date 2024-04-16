#include <stdio.h>
#include <pthread.h>

// buffer
int buffer[10];

void random_expression(i)
{
    int op1, op2, operator;
    operator = random(1, 4);
    switch (operator)
    {
        case(1):
            buffer[i] = op1 + op2;
            break;
        case(2):
            buffer[i] = op1 - op2;
            break;
        case(3):
            buffer(i) = op1 * op2;
            break;
        case(4):
            buffer[i] = op1 / op2;
            break;
    }
}

void producer1()
{
    for(int i = 0; i < 20; i++)
    if buffer.size() < 10{
        random_expression(i);
    }
}


int main()
{

}

//Dataclass which makes random expression and stores the expresion and producer which requested it
class expression_dataclass
{
    int expression;
    int producer;
}
