#include <stdio.h>

int main(void)
{

    int m,temp=0,div=0;
    scanf("%d",&m);
    while(m--)
    {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        if(a <= 3)
            printf("%d\n",a*b);
        else
        {
            int sum = (a*b);
            div = a/3;
            temp = a - div*3;
            if(temp == 0)
            {
                printf("%d\n",(div-1)*c + sum);
            }
            else printf("%d\n",div*c+sum);
        }
    }
    return 0;
}
