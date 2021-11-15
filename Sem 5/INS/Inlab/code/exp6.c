#include <stdio.h>
#include <string.h>
void main(){

char a[10];
char pass[] = "abcdxyzw";
printf("Enter The Password: ");
gets(a);
if (strcmp(a, pass)==0){
    printf("Correct Password");
}
else{
    printf("Incorrect Password");
}

}
