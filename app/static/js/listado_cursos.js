(function (){
    const btnsComprarCurso = document.querySelectorAll('.btnComprarCurso');
    
    let idCursoSeleccionado = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;

    btnsComprarCurso.forEach((btn) => {
        btn.addEventListener('click', function () {
            idCursoSeleccionado = this.id;
            confirmarCompra();
        });
    });
    const confirmarCompra = ()=>{
        Swal.fire({
            title: '¿Confirma la compra del curso seleccionado?',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'Comprar',
            showLoaderOnConfirm: true,
            preConfirm: async () => {
                // console.log(window.origin);
                return await fetch(`${window.origin}/comprarCurso`, {
                    method: 'POST',
                    mode: 'same-origin',
                    credentials: 'same-origin',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrf_token
                    },
                    body: JSON.stringify({
                        'id': idCursoSeleccionado
                    })
                }).then(response => {
                    if (!response.ok) {
                        notificacionSwal('Error', response.statusText, 'error', 'Cerrar');
                    }
                    return response.json();
                }).then(data => {
                    if (data.exito) {
                        notificacionSwal('¡Éxito!', 'Curso Comprado', 'success', '¡Ok!');
                    } else {
                        notificacionSwal('¡Alerta!', data.mensaje, 'warning', 'Ok');
                    }
                }).catch(error => {
                    notificacionSwal('Error', error, 'error', 'Cerrar');
                });
            },
            allowOutsideClick: () => false,
            allowEscapeKey: () => false
        });   
    }; 
})();