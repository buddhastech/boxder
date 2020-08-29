
let statusCtx = document.getElementById('status-chart');

let statusChart  = new Chart(statusCtx, {
    type:"pie",
    data:{
        labels: ['Activo', 'Suspendido', 'De baja'],
        datasets:[{
            label: 'Activos',
            data: [6, 10, 2],
            backgroundColor:[
                "rgba(57, 127, 50, 0.9)",
                "rgba(255, 213, 0, 0.9)",
                "rgba(172, 38, 36, 0.9)"
                ]
            }]
        }
    });

    let priceCtx = document.getElementById('price-assets').getContext('2d');

    let chartPrice  = new Chart(priceCtx, {
        type:"bar",
        data:{
            labels: ['Activo', 'Suspendido', 'De baja', "e", "e"],
            datasets:[{
                label: 'Activos',
                data: [6, 10, 2, 44, 72],
                backgroundColor:[
                    "rgba(57, 127, 50, 0.9)",
                    "rgba(255, 213, 0, 0.9)",
                    "rgba(172, 38, 36, 0.9)",
                    "rgba(172, 38, 36, 0.9)",
                    "rgba(172, 38, 36, 0.9)"
                    ]
                }]
            }
        });