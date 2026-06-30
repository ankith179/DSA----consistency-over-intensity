class Solution {
    public int numberOfSubstrings(String Str) {
        int i, count = 0;
        int last[] = new int[] {-1, -1, -1};
        for (i = 0; i < Str.length(); i++) {
            if(Str.charAt(i) == 'a') last[0] = i;
            else if(Str.charAt(i) == 'b') last[1] = i;
            else if(Str.charAt(i) == 'c') last[2] = i;
            int left = Math.min(Math.min(last[0], last[1]), last[2]);
            //count += (left+1)
            count=count+(left+1);
        }
        return count;
    }
}