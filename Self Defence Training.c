#include <stdio.h>

int main(void) {
	// your code goes here
	int m,i;
	scanf("%d",&m);
	while(m--){
	    int n,count=0;
	    scanf("%d",&n);
	    for ( i =0; i<n; i++){
	        int x;
	        scanf("%d",&x);
	        if(x >= 10 && x <= 60)
	            count++;
	    }
	    printf("%d\n",count);
	}
	return 0;
}
