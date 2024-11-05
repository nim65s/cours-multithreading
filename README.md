# Cours Multithreading

Support de cours multithreading 3A SRI 2024-2025

## Lancement d’une tâche longue

Affiche le temps nécessaire à la résolution d’un problème linéaire de taille 6000

```bash
$ ./task.py
task: 2.6477803950001544
```

## Lancement de plusieurs sous processus

```bash
$ ./sub.py
task: 10.228055024000241
task: 10.310156592000567
[…]
task: 10.578246373000184
total: 11.593499044000055
mean: 0.7245936902500034
```

## Lancement d’un pool de process

```bash
$ ./pool.py
task: 10.485880100999566
task: 10.470191663999685
[…]
task: 10.754035089999888
total: 23.090329153999846
mean: 0.7215727860624952
```

NB: on peut facilement remplacer `Process` par `Thread` dans ce programme, mais en pratique c’est contre-productif dans
ce cas.
