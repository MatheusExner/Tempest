#include <cstring>
#include <limits.h>
#include <stdio.h>

void processar_dado(unsigned int tamanho_dado, char nome)
{
    const char *message = "Iniciando programa...";
    // const char message[] = "Iniciando programa...";
    char destination[sizeof(message) + tamanho_dado];
    // char* destination = (char*)malloc(strlen(nome) + strlen(message) + 1);
    strncpy(destination, nome, sizeof(destination) - 1);

    //if (destination != NULL)
    //{
    //    strcpy(destination, message);
    //    strcat(destination, nome);

    //    printf("Destination: %s\n", destination);

    //    free(destination); // Free the dynamically allocated memory
    //}
}

int main()
{
    processar_dado(UINT_MAX, "nome");
    return 0;
}