function dataFromServer(data){
    
    if(data == '1'){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Registro con éxito',
            showConfirmButton: true
          });

    }else{
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'No se han podido procesar sus datos,',
          });
    }

}