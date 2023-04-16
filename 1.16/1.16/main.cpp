#include <iostream>

std::string code = "TGEEMNELNNTDROEOAAHDOETCSHAEIRLM";
int arr[10]={0,1,2,3,4,5,6,7,8,9};

int count = 0;

void permutation(int step, int end){
    if(step==end){
        count++;
//        printf("%d : ",count);
//        for(int i=0;i<end;i++){
//            printf("%d ",arr[i]);
//        }
//        printf("\n");
        std::string output = "0123456789012345678901234567890123456789";
        for(int i=0;i<code.length();i+=end){
            for(int j=0;j<end;j++){
                output[j+i]=code[arr[j]+i];
            }
        }
        std::cout<<output<<std::endl;
    }
    else{
        for(int i=step;i<end;i++){
            std::swap(arr[i],arr[step]);
            permutation(step+1,end);
            std::swap(arr[i],arr[step]);
        }
    }
}

int main() {


    permutation(0,5);

//    int p = 1;
//    for(int i=2;i<=10;i++){
//        p = p*i;
//        std::cout<<p<<" ";
//    }
    return 0;
}
