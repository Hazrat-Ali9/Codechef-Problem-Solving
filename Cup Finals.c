#include <stdio.h>

int main(void)
{

    int m;
    scanf("%d",&m);
    while(m--)
    {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        if(a>=b)
        {
            if(a-b > c)
                printf("NO\n");
            else printf("YES\n");
        }
        else
        {
            if(b-a > c)
                printf("NO\n");
            else printf("YES\n");
        }
    }
    return 0;
}
