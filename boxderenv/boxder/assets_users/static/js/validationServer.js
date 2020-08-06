function dataFromServer(data){
    
    if(data == '1'){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Registro con éxito',
            showConfirmButton: false,
            timer: 1500
          });

    }else{
        Swal.fire({
            icon: 'error',
            title: 'Ha ocurrido un error, vuelve a intentarlo',
            text: 'Something went wrong!',
            footer: '<a href>Why do I have this issue?</a>'
          });
    }

}