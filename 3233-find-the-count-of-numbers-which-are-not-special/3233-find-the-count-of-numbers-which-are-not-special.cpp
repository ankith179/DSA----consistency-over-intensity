int constexpr mx = 31622;
vector<int> p;
class Solution {
public:
int nonSpecialCount(int l, int r) {
    if (p.empty()) {
        bool sieve[mx] = {};
        for (int i = 2; i < mx; ++i)
            if (!sieve[i])
                for (int j = i * i; j < mx; j += i)
                   sieve[j] = true;
        for (int i = 2; i < mx; ++i)
            if (!sieve[i])
                p.push_back(i * i);
    }
    auto lp = lower_bound(begin(p), end(p), l), rp = upper_bound(lp, end(p), r);
    return r - l + 1 - (rp - lp);
}
};