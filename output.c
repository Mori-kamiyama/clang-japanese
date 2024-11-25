#include <stdio.h>

int main(void){
	for (int い = 0; い < 100;い ++){
        if(い % 15 == 0){
			printf("ふぃずばず\n");
		}else if(い % 3 == 0){
			printf("ふぃず\n");
		}else if(い % 5 == 0){
			printf("ばず\n");
		}else{
		    printf("%d\n", い);
		}
	}

	return 0;
}
