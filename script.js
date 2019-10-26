var pos_vitoria = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
var id_btns     = ['btn0','btn1','btn2','btn3','btn4','btn5','btn6','btn7','btn8'];
var lista       = ['n','n','n','n','n','n','n','n','n'];
var ganhou      = [];
var vez         = 'x';
var velha       = 0;

function restart(){
	velha = 0;
	colorir_botoes(id_btns,'red','red');

    var lista  = ['n','n','n','n','n','n','n','n','n'];
    var ganhou = [];
    var vez    = 'x';

    for (i=0; i < id_btns.length; i++){
    	document.getElementById(id_btns[i]).innerText = 'n';
    }
}

function clique(btn){
	if (btn.innerText == 'n'){
		velha++;
 		btn.innerText = vez;
        btn.style.color = 'white';

		verifica = verifica_vitoria(btn);
		if ( verifica.length != 0){
			colorir_botoes(verifica,'white','blue');
		}
		
		troca_vez();

	} else {
		alert("Ai já está preenchido!");
	}
}

function troca_vez(){
	if (vez == 'x'){
		vez = 'o';
	} else {
		vez = 'x';
	}	
}

function verifica_vitoria(btn){
    var ganhou = [];

	for (i = 0; i < pos_vitoria.length; i++){

		var id_a = id_btns[pos_vitoria[i][0]];
		var id_b = id_btns[pos_vitoria[i][1]];
		var id_c = id_btns[pos_vitoria[i][2]];

		var a = document.getElementById(id_a).innerText;
		var b = document.getElementById(id_b).innerText;
		var c = document.getElementById(id_c).innerText;

		if ( ( a == vez) && (b == vez) && (c == vez)){
			ganhou.push(id_a,id_b,id_c); 
		}
	}

	return ganhou;
}

function colorir_botoes(verifica,fg,bg){
	for (i = 0; i < verifica.length; i++){
		document.getElementById(verifica[i]).style.backgroundColor = bg;
		document.getElementById(verifica[i]).style.color = fg;
	}
}
