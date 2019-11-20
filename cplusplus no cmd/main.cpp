#include <iostream>
#include <locale.h>

/*
    Autor: Gabriel Gregório da Silva
    github: https://github.com/gabrielogregorio/
    Descrição: Meu primeiro jogo da velha em c++    
*/
using namespace std;

char  tabuleiro[9];
int posicaoEscolher;
char vez = 'x';
int velha = 0;

int renderizar(){
    
    int valor = 0;

    for (int x= 1; x<4; x++){

        for (int i=1; i < 4; i++){
            cout << tabuleiro[ valor ] << '|';
            valor += 1;
        }

        if (x != 3)
            cout << endl << "-+-+-+-";

        if (x != 4)
            cout << endl;
    }
    return 0;
}

int resetarTabuleiro(){
    velha = 0;

    for (int i=0; i < 9; i++){
        tabuleiro[i] = ' ';
    }

    return 0;
}

int escolhePosicao(){        
    cout <<  "Escolha uma posição: " ;
    cin >> posicaoEscolher;
    return posicaoEscolher;
}

int trocaVez(){
    if (vez == 'x')
        vez = 'o';
    else
        vez = 'x';
}

int verificaVelha(){
    if (velha == 9)
        return 1;
    else
        return 0;
}

int verificaVitoria(){    
    int posicoesDeVitoria[8][3] = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6} };

    for (int x = 0; x < 8 ; x++){
        /* Houve uma vitória */
        if ( (tabuleiro[posicoesDeVitoria[x][0]] == vez) && ( tabuleiro[posicoesDeVitoria[x][1]] == vez) && (tabuleiro[posicoesDeVitoria[x][2]] == vez) ){
            system("cls");
            renderizar();

            cout << "Jogador '" << vez << "' você ganhou!" << endl;

            system("pause");
            system("cls");
            return 1;
        }
    }
    return 0;
}

int main(){
    setlocale(LC_ALL,"portuguese");

    resetarTabuleiro();

    int posicao;    
    int statusVitoria;

    while (true){
        statusVitoria = 0;
        renderizar();    
        posicao = escolhePosicao();
        
        if (tabuleiro[posicao] == ' '){
            tabuleiro[posicao] = vez;
            velha += 1;
            
            statusVitoria = verificaVitoria();
            
            if (statusVitoria == 0){
                
                if (verificaVelha() == 1){
                    cout << "Deu velha pessoal!" << endl;
                    system("pause");
                    resetarTabuleiro();
                } else {
                    trocaVez();            
                }
                system("cls");                    
                    
            } else {
                resetarTabuleiro();
            }
        } else {
            system("cls");
            cout << "Essa posição já está oculpada!" << endl;
        }
    }
    return 0;
}