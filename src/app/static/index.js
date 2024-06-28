window.onload = init

function init() {
    const form = document.getElementById("form")
    const recomendaciones = document.getElementById("recomendaciones")

    form.onsubmit = (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const formObject = Object.fromEntries(formData.entries())
        fetch("/recomendaciones", {
            method: "POST",
            body: JSON.stringify(formObject),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(res => res.json())
        .then(data => {
            const {views, likes, dislikes, dia_semana, tags}  = data
            
            text = ""
            text += `<li>La cantidad de views que puedes tener es: <span class="text-violet-500">${views}</span></li>`
            text += `<li>La cantidad de likes que puedes tener es: <span class="text-emerald-500">${likes}</span></li>`
            text += `<li>La cantidad de dislikes que puedes tener es: <span class="text-rose-600">${Math.abs(dislikes)}</span></li>`
            
            if(dia_semana == "hoy"){
                text += "<li>Has elegido el mejor día para subir tu video!</li>"
            }else {
                text += `<li>El mejor día para subir tu video es el <span class="text-amber-500">${dia_semana}</span></li>`
            }
            if(tags){
                text += `<li>Debería incluir alguno de estos tags: <span class="text-fuchsia-400">${tags.join(', ')}</span></li>`
            }
            recomendaciones.innerHTML = `<ul class="text-white">${text}</ul>`
        })
    }

}