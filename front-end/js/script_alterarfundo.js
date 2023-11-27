$(function () {

    $(document).on("click", "#enviar", function () {

        var imagem = new FormData($('#formulario')[0]);

        $.ajax({
            url: 'http://localhost:5000/salvar_img',
            method: 'POST',
            data: imagem, 
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                if (data.resultado == "ok"){
                    alert(data.resultado + " " + data.detalhes);
                }else{
                    alert(data.resultado + data.detalhes);    
                };
            },
            error: function (data) {
                alert("Não foi possível enviar a imagem, back-end indisponível");
            }
        });
    });
});