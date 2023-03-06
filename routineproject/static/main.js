let date = document.getElementsByClassName('date');
let date2 = Array.from(date);



for(var i = 0; i < date2.length; i++){
    let classDate = new Date(date2[i].innerHTML).getTime();
    let todayDate = new Date().getTime();
    let status = document.getElementsByClassName('status');
    let routine = document.getElementsByClassName('routine');
    let routine2 = Array.from(routine);
    let status2 = Array.from(status);

    if(classDate > todayDate){
        status2[i].innerHTML = 'Upcoming';
    }
    else if((classDate+172800000) > todayDate ){
        status2[i].innerHTML = 'Completed';
    }
    else{
        routine2[i].style.display = 'none';
    }
}



//upcomming 

function Upcoming() {
    let sts = document.getElementsByClassName('status');
    let sts2 = Array.from(sts);
    let tr = document.getElementsByClassName('routine');
    let tr2 = Array.from(tr);
    for(let i = 0; i < tr2.length; i++){
        if(sts2[i].innerHTML == 'Completed'){
            tr2[i].style.display = 'none';
        }
        else{
            continue;
        }
    }
}


//extra feature














