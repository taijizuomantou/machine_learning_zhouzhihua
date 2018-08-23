#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int N = 5;
int num = 0;
int k;
int v[N][N][N];

bool judge(int a,int b,int c)
{
    //printf("aaa");
    if(v[a][b][c])
        return false;
    if(a == 0 && b == 0 && c == 0)
    {
        for(int i = 0; i < 3; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                for(int l = 0; l < 4; l ++)
                {
                    if(v[i][j][l])
                        return false;
                }
            }
        }
    }
    if(a == 0 && b == 0)
    {
        for(int i = 0; i < 3; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                if(v[i][j][c] || v[i][j][0])
                    return false;
            }
        }
    }
    if(a == 0 && c == 0)
    {
        for(int i = 0; i < 3; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                if(v[i][b][j] || v[i][0][j])
                    return false;
            }
        }
    }
    if(b == 0 && c == 0)
    {
        for(int i = 0; i < 4; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                if(v[a][i][j] || v[0][i][j])
                    return false;
            }
        }
    }
    if(a == 0)
    {
        for(int i = 0; i < 3; i ++)
        {
            if(v[i][b][c]||v[i][0][c]||v[i][b][0]||v[i][0][0])
                return false;
        }
    }
    if(b == 0)
    {
        for(int i = 0; i < 4; i ++)
        {
            if(v[a][i][c]||v[0][i][c] || v[a][i][0]||v[0][i][0])
                return false;
        }
    }
    if(c == 0)
    {
        for(int i = 0; i < 4; i ++)
        {
            if(v[a][b][i]||v[0][b][i] || v[a][0][i]||v[0][0][i])
                return false;
        }
    }



    if(v[0][b][c] || v[a][0][c] || v[a][b][0] || v[0][0][c] || v[0][b][0] ||v[a][0][0]||v[0][0][0])
        return false;
    return true;
}
void dfs(int bi,int bj ,int bl,int layer)
{
    if(layer == k)
    {
        for (int i = 0; i < 3; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                for(int l = 0; l < 4; l ++)
                {
                    //if(v[i][j][l] != 0)
                   // printf("%d %d %d\n",i,j,l);
                }
            }
        }
        //printf("%d%d%d\n",bi,bj,bl);
        num = num + 1;
        return;
    }
    v[bi][bj][bl] = 1;
    bool tf1 = false;
    bool tf2 = false;
    for (int i = bi; i < 3; i ++)
    {
        for (int j = 0; j < 4; j ++)
        {
            if(i == bi && tf1 == false)
            {
                j = bj;
                tf1 = true;
            }
            for(int l = 0; l < 4; l ++)
            {
                if(i == bi && tf2 == false)
                {
                    l = bl;
                    tf2 = true;
                }
                //是0的数字前面出现了其他数字相等或者是0
                //如果两个可以通过通配符相互转化则不行
/*                a b c
                i j l
                x y
                x == y
                x == 0 || y == 0
                */
                if(judge(i,j,l))
                    dfs(i,j,l,layer+1);

            }
        }
    }
    v[bi][bj][bl] = 0;
    return;
}
int main()
{
    memset(v,0,sizeof(v));
    int allnum = 0;
    for(k = 1; k < 19; k ++)
    {
        //k = 18;
        num = 0;
        for(int i = 0; i < 3; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                for(int l = 0; l < 4; l ++)
                {
                    dfs(i,j,l,1);
                }
            }
        }
        printf("%d   %d\n",k,num);
        allnum = num + allnum;
    }
    printf("%d\n",allnum);
    return 0;
}
