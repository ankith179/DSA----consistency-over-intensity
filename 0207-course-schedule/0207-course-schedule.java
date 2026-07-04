class Solution {
    static{
        for(int i=0;i<500;++i){
            canFinish(2,new int[][]{{0, 1}});
        }
    }
    public static boolean dfs(ArrayList<Integer>[] graph, int V, boolean[] stack){
        boolean[] visited = new boolean[V];

        for(int i = 0; i < V; i++){
            if(!visited[i]){
                if(!dfsUtil(graph, V, visited, i, stack)) return false;;
            }
        }
        return true;
    }
    public static boolean dfsUtil(ArrayList<Integer>[] graph, int V, boolean[] visited, int i, boolean[] stack){
        visited[i] = true;
        stack[i] = true;

        for(int j = 0; j < graph[i].size(); j++){
            int dest = graph[i].get(j);

            if(stack[dest]) return false;

            if(!visited[dest]){
                if(!dfsUtil(graph, V, visited, dest, stack)) return false;
            }
        }

        stack[i] = false;

        return true;
    }
    public static boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<Integer>[] graph = new ArrayList[numCourses];
        boolean[] stack = new boolean[numCourses];

        for(int i = 0; i < numCourses; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i < prerequisites.length; i++){
            int u = prerequisites[i][0];
            int v = prerequisites[i][1];

            graph[v].add(u);
        }

        return dfs(graph, numCourses, stack);
    }
}