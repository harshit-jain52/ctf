# GoLogicFlaw

Given file:

```go
package main

import (
  "bufio"
  "fmt"
  "math/rand"
  "os"
  "strconv"
  "strings"
  "time"
)

func generateRandomNumber() int {
  rand.Seed(time.Now().UTC().Unix())
  return rand.Intn(1000000000)
}

func log(s string) {
  fmt.Println(fmt.Sprintf("[%d] %s", time.Now().UTC().Unix(), s))
}

func guessANumber(count int) bool {
  randNumber := generateRandomNumber()

  log(fmt.Sprintf("number %d: ", count))
  reader := bufio.NewReader(os.Stdin)
  line, err := reader.ReadString('\n')
  if err != nil {
    fmt.Println(err)
    os.Exit(1)
  }
  number, err := strconv.Atoi(strings.TrimSpace(line))
  if err != nil {
    fmt.Println(err)
    os.Exit(1)
  }

  if number == randNumber {
    return true
  }

  log(fmt.Sprintf("Guess failed: %d != %d", number, randNumber))
  return false
}

func win() {
  content, err := os.ReadFile("/flag")
  if err != nil {
    log("Unable to read the flag.")
    return
  }
  log(fmt.Sprintf("Here is your flag: %s", string(content)))
}

func main() {
  log("Guess three random numbers and win the flag!")
  for i := 1; i <= 3; i++ {
    success := guessANumber(i)
    if !success {
      log("No flag for you. bye bye ..")
      return
    }
  }
  win()
}
```

The core bug is reseeding the random number generator every time with time.Now().Unix(), which has only 1-second resolution and is also logged. \
Here is a go script to get the random number from a given timestamp:

```go
package main

import (
    "fmt"
    "math/rand"
)

func main() {
    var timestamp int64
    fmt.Scan(&timestamp)

    r := rand.New(rand.NewSource(timestamp))
    fmt.Println(r.Intn(1000000000))
}
```

Connecto to server, pass the timestamp printed to the above script and input the generated number. Do this 3 times.
