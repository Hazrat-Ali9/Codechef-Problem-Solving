#include <stdio.h>
#include <limits.h>
#include<stdlib.h>
int main(void) {

	int p;
	scanf("%d",&p);
	while(p--){
	    int x1,y1,x2,y2;
	    scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
	    int a = abs(x1-x2);
	    int b=abs(y1-y2);
	    if(a > b)
	    printf("%d\n",a);
	    else printf("%d\n",b);
	}
	return 0;
}
