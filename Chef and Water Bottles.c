#include <stdio.h>

int main(void) {
	
	int m,sum=0;
	scanf("%d",&m);
	while(m--){
	    int a,b,c;
	    scanf("%d %d %d",&a,&b,&c);
	    sum = c/b;
	    if(sum >= a){
	        printf("%d\n",a);
	    }
	    else printf("%d\n",sum);
	}
	return 0;
}

