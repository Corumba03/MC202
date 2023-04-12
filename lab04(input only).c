#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 51
#define MAX_NAMES 10

void input(char names_1[MAX_NAMES][MAX_LENGTH], char names_2[MAX_NAMES][MAX_LENGTH]){
    char input_string[MAX_LENGTH];
    int i = 0;
    while (fgets(input_string, MAX_LENGTH, stdin) != NULL && i < 3){
        // Find the position of " conhece " in the input string
        char *token = strstr(input_string, " conhece ");

        // Copy the characters before and after " conhece " into the name arrays
        strncpy(names_1[i], input_string, token - input_string);
        names_1[i][token - input_string] = '\0';
        strncpy(names_2[i], token + strlen(" conhece "), MAX_LENGTH);
        names_2[i][strlen(names_2[i]) - 1] = '\0'; // Remove the newline character at the end of the second name

        // Print the contents of the name arrays
        printf("Name 1: %s\n", names_1[i]);
        printf("Name 2: %s\n", names_2[i]);
        i++;
    }
}
