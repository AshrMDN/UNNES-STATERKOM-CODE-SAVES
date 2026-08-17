# 🚀 UNNES Staterkom: My C++ Evolution Arc

Hey there, fellow Discord adventurers! 🎮 Welcome to the secret laboratory where I turn coffee, sleepless nights, and pure willpower into functional C++ code. 

This repository tracks my coding journey for the **Staterkom** (Starter Komputer) course at Universitas Negeri Semarang (UNNES). If you're from my Discord server, congrats! You found the source code behind my chaotic testing.

---

## 🔥 Current Milestone: The "Kasian Dit" Incident
Yes, the compiler bullied me at first because C++ reads code from top to bottom (who knew, right?). But after a quick training arc, it finally works! 

Here is the legendary snippet that brought this repo to life:
```cpp
string printerKata(string name) {
    return "yahaha kasian " + name; 
}
```

---

## 🛠️ Supercharged Tech Stack
Unlike standard boring templates, this setup is customized for ultimate performance and portability:
* 🏎️ **Fast I/O Enabled:** Using `ios_base::sync_with_stdio(false)` because waiting for terminal input is for the weak.
* 📦 **Dynamic Ready:** Pre-loaded with `<vector>` and `<string>` for big-brain data handling.
* 🛡️ **Static Linked Exe:** Compiled with `-static-libstdc++` so the executables don't crash with *missing DLL* errors when sent over Discord.

---

## 💻 How to Run This Chaos Locally

If you want to clone this and test it out on your own machine without Windows screaming at you, use this ultimate compile command in your terminal:

```bash
g++ firstDemo.cpp -o firstDemo.exe -static -static-libgcc -static-libstdc++
```

Then run it like a pro:
```powershell
& ".\firstDemo.exe"
```

---

## 🤖 Discord Crew Credits
Shoutout to the bugs that kept me company, the `int main()` function for being the only reason my code actually starts, and the Discord homies who didn't believe my code would compile. **IT WORKS NOW, Y'ALL!** 😎

*Feel free to leave a ⭐ star on this repository if you want to support my journey to not failing this semester!*
