#include <stdio.h>
int main(void) {

	int m,even=0,odd=0;
	scanf("%d",&m);
	for(int i =0; i<m; i++){
	    int h;
	    scanf("%d",&h);
	    if(h%2 == 0)
	        even += 1;
	    else
	        odd +=1;
	}
	if(even > odd)
	        printf("READY FOR BATTLE\n");
	    else printf("NOT READY\n");
	return 0;
}
