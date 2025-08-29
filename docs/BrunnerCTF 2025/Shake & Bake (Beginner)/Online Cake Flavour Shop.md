# Online Cake Flavour Shop

> Pwn

```text
Brunnerne made an online flavour shop! Your wildest dreams can be fulfilled, it's actually hard to WRAP your head AROUND how amazing this software is!
```

points: `40`

solves: `476`

author: `olexmeister`

---

We are given a C file `shop.c`:

```c
#include <stdio.h>
#include <stdlib.h>

#define FLAG_COST 100
#define BRUNNER_COST 10
#define CHOCOLATE_COST 7
#define DRØMMEKAGE_COST 5


int buy(int balance, int price) {
    int qty;
    printf("How many? ");
    scanf("%u", &qty);

    int cost = qty * price;
    printf("price for your purchase: %d\n", cost);

    if (cost <= balance) {
        balance -= cost;
        printf("You bought %d for $%d. Remaining: $%d\n", qty, cost, balance);
    } else {
        printf("You can't afford that!\n");
    }

    return balance;
}

void menu() {
    printf("\nMenu:\n");
    printf("1. Sample cake flavours\n");
    printf("2. Check balance\n");
    printf("3. Exit\n");
    printf("> ");
}

unsigned int flavourMenu(unsigned int balance) {
    unsigned int updatedBalance = balance;

    printf("\nWhich flavour would you like to sample?:\n");
    printf("1. Brunner ($%d)\n", BRUNNER_COST);
    printf("2. Chocolate ($%d)\n", CHOCOLATE_COST);
    printf("3. Drømmekage ($%d)\n", DRØMMEKAGE_COST);
    printf("4. Flag Flavour ($%d)\n", FLAG_COST);
    printf("> ");

    int choice;
    scanf("%d", &choice);

    switch (choice)
    {
    case 1:
        updatedBalance = buy(balance, BRUNNER_COST);
        break;
    case 2:
        updatedBalance = buy(balance, CHOCOLATE_COST);
        break;
    case 3:
        updatedBalance = buy(balance, DRØMMEKAGE_COST);
        break;
    case 4:
        unsigned int flagBalance;
        updatedBalance = buy(balance, FLAG_COST);
        if (updatedBalance >= FLAG_COST) {
            // Open file and print flag
            FILE *fp = fopen("flag.txt", "r");
            if(!fp) {
                printf("Could not open flag file, please contact admin!\n");
                exit(1);
            }
            char file[256];
            size_t readBytes = fread(file, 1, sizeof(file), fp);
            puts(file);
        }
        break;
    default:
        printf("Invalid choice.\n");
        break;
    }

    return updatedBalance;
}

int main() {
    int balance = 15;
    int choice;

    printf("Welcome to Overflowing Delights!\n");
    printf("You have $%d.\n", balance);

    while (1) {
        menu();
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            balance = flavourMenu(balance);
            break;
        case 2:
            printf("You have $%d.\n", balance);
            break;
        case 3:
            printf("Goodbye!\n");
            exit(0);
            break;
        default:
            printf("Invalid choice.\n");
            break;
        }
    }
    return 0;
}
```

We need to buy the flag (cost = 100) with our balance (15)

`buy()` function also takes `qty` as input which is then multiplied by `price` before comparing with `balance` \
If `qty` = INT_MAX (**2147483647**) is provided, `qty*100` evaluates to **-100**, because of integer overflow wrap-around, this satisfies the condition of being less than balance and hhence flag is printed
