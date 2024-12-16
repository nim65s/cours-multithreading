#include <chrono>
#include <iostream>
#include <omp.h>
#include <vector>

auto main() -> int {

#pragma omp parallel
  {
    std::string r = "hello ";
    r.append(std::to_string(omp_get_thread_num()));
    r.append("\n");

#pragma omp critical
    { std::cout << r; }
  }

  const int N = 1000000000;
  std::vector<int> v(N, 0);
  const auto start = std::chrono::steady_clock::now();
#pragma omp parallel for
  for (int i = 0; i < N; i++) {
    v[i] = i * i;
  }
  const auto end = std::chrono::steady_clock::now();

  const auto d = end - start;
  std::cout << "temps écoulé: " << d.count() / 1000000000. << std::endl;

  return EXIT_SUCCESS;
}
