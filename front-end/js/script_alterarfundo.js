$(function () {

    $(document).on("click", "#enviar", function () {

        var imagem = new FormData($('#formulario')[0]);

        //var imagem = $("#imagem").val();
        console.log(imagem)

        $.ajax({
            url: 'http://localhost:5000/salvar_img',
            method: 'POST',
            data: imagem, 
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                alert("Enviou a imagem direitinho!");
            },
            error: function (data) {
                alert("Não foi possível enviar a imagem");
            }
        });
    });
});