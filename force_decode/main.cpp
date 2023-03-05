/* 5/3/2023
 * tjcloudwaker
 * 密码学原理与实践
 * 习题1.5
 * */
#include <iostream>
#include <string>

int main() {
    std::string code = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD";
    for(int i=0;i<=25;i++){
        for(auto &j:code){
            std::cout<<char((j-'A'+i)%26+'A');
        }
        std::cout<<"\n";
    }
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
