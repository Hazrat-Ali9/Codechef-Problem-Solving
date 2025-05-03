#include <stdio.h>

int main(void) {

	int m;
	scanf("%d",&m);
	while(m--){
	    int x,y;
	    scanf("%d %d",&x,&y);
	    if(x>y){
	        int sum = x-y;
	        printf("%d\n",sum+x);
	    }
	    else{
	        printf("%d\n",x);
	    }
	}
	return 0;
}
