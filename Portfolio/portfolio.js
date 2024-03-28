let menu=document.getElementById('menuicon')

menu.addEventListener('click',function (){
    let rnav=document.getElementById('rightnavigation')
    
    rnav.style.visibility='visible'
    
    
    let home=document.getElementById('home')
    home.style.display='block'
   
    
})

let closeicon=document.getElementById('closeicon')
closeicon.addEventListener('click',function (){
    let rnav=document.getElementById('rightnavigation')
    
    rnav.style.visibility='hidden';
    
    let home=document.getElementById('home')
    home.style.display='none';
     
})

