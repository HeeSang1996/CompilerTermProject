int main() {
    int iteration = 5;
    bool logic = true;
    
    while (iteration) {
        printf(iteration);
        if (iteration == 5){
            printf("First")
        } else {
            printf("Iteration ");
        }
        iteration = iteration - 1;
    }

    return 0;
}