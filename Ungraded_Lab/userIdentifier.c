#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    union {
        int int_id;
        char *str_id;
    };
} userIdentifier;

void printUser(userIdentifier user) {
    if (user.str_id) {
        printf("User ID: %s\n", user.str_id);
    } else {
        printf("User ID: %d\n", user.int_id);
    }
}

int main() {
    // Integer ID
    userIdentifier user1 = {.int_id = 1234};
    printUser(user1); // Output: User ID: 1234

    // String ID
    userIdentifier user2;
    user2.str_id = strdup("JohnDoe");
    printUser(user2); // Output: User ID: JohnDoe

    free(user2.str_id);

    return 0;
}
