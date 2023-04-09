<div class="panel-body">
    <span id="user_id" data-id="4547"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>You have <code>n</code> number of locked boxes in front of you. 
Each box is numbered sequentially from <code>0</code> to <code>n - 1</code> and each box may contain keys to the other boxes. </p>

<p>Write a method that determines if all the boxes can be opened.</p>

<ul>
<li>Prototype: <code>def canUnlockAll(boxes)</code></li>
<li><code>boxes</code> is a list of lists</li>
<li>A key with the same number as a box opens that box</li>
<li>You can assume all keys will be positive integers

<ul>
<li>There can be keys that do not have boxes</li>
</ul></li>
<li>The first box <code>boxes[0]</code> is unlocked</li>
<li>Return <code>True</code> if all boxes can be opened, else return <code>False</code></li>
</ul>

<pre><code>carrie@ubuntu:~/lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/lockboxes$
</code></pre>

<pre><code>carrie@ubuntu:~/lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/lockboxes$
</code></pre>

  </div>