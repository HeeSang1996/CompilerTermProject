void main() {
    bool a=true;
    int buf = 0;
    int buf2 = 0;

    if(a){}
    if(a) {}
    if (a){}
    if (a) {}

    if(a){
        buf++;
    }
    if(a) {
        buf++;
    }
    if (a){
        buf++;
    }
    if (a) {
        buf++;
    }

    if(a)
    {
        buf++;
    }
    if (a)
    {
        buf++;
    }

    if(a){
        buf++;
    }else{
        buf2++;
    }
    if(a){
        buf++;
    }else {
        buf2++;
    }
    if(a){
        buf++;
    } else{
        buf2++;
    }
    if(a){
        buf++;
    } else {
        buf2++;
    }

    if(a){
        buf++;
    }else if{
        buf2++;
    }else{
        buf2++;
    }
    if(a){
        buf++;
    } else if{
        buf2++;
    }else{
        buf2++;
    }
}