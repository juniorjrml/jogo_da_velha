var id = document.getElementById('id_tabuleiro3');
$.ajax({
    url: '/tabuleiro/atualizar/'+id.value,
    method: 'get',

}).done(function (resposta){
    window.setTimeout(function (){
        $('#jogo_da_velha_tabuleiro').html(resposta);
    },1000)
})
