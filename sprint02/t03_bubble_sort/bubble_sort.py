def bubble_sort(bubkist):
    for i in range(len(bubkist)):
        for a in range(len(bubkist) - 1):
            if bubkist[a] > bubkist[a+ 1] :
                bubkist[a] , bubkist[a+ 1]  = bubkist[a + 1] , bubkist[a]

