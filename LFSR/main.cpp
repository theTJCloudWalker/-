// 一个4位LFSR的C语言实现
#include<iostream>
#include <bitset>//二进制
#include <stdio.h>
#define N 4 // 寄存器位数
#define TAP1 0 // 第一个抽头位
#define TAP2 3 // 第二个抽头位

int count_bits(int n) {
    int count = 0;
    while (n != 0) {
        n &= (n - 1);  // 将最右边的1变成0
        count++;
    }
    return count;
}


int main()
{
    for(int i=0;i<16;i++){
        std::cout <<"["<<i<< "]  initial vector: " << std::bitset<sizeof(i)*1>(i) << std::endl;
        //printf("initial vector: %s \n", i); // 打印周期
        unsigned int lfsr = i; // 初始状态为1001
        unsigned int bit; // 存储异或结果
        unsigned int period = 0; // 记录周期

        do {
            // 1.18
            // Zi+4 = (Zi + Zi+1 + ~~~ + Zi+3) mod 2
            //bit = count_bits(lfsr) % 2;

            //1.19
            // Zi+4 = (Zi + Zi+3) mod 2
            bit = ((lfsr >> TAP1) + (lfsr >> TAP2)) % 2 ;
            lfsr = (lfsr >> 1) | (bit << (N - 1)); // 右移一位并填充最左边一位
            ++period;
            printf("    Current state: %u\n", lfsr); // 打印当前状态
        } while(lfsr != i); // 循环直到回到初始状态

        printf("  Period: %u\n", period); // 打印周期
    }



    return 0;
}