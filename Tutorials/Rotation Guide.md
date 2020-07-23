---


---

<p>back to the <a href="../Tutorials.md">Tutorials</a>.</p>
<h1 id="rotations">Rotations</h1>
<p>You might have heard of rotation values like roll, yaw and pitch. But what are they exactly and the most important question:<br>
<strong>How do they work in particle effects?</strong><br>
We’ll answer this question in this guide.</p>
<h2 id="basic-knowledge">Basic Knowledge</h2>
<p>Every particle object has an orientation in the local space. Often we simply use <code>Render sprites</code> and don’t have to think much about it. But if we do, we need to know the following:</p>
<p>Each particle has a normal vector. This is a vector which is perpendicular to an object. Let’s say we have an sprite. This sprite is an 2D object about which you could say that it represents a plane. Now this normal vector is perpendicular to that plane:<br>
<img src="https://i.imgur.com/cxU2bO3.png" alt=""><br>
The arrow in this picture is representing that normal vector. A rotation of this vector would also cause the plane, and therefore the sprite to rotate. In this example the sprite was aligned to <code>World-Z</code>, because it is a good representation. If we’d use the most commonly used align, <code>Screen Align</code>, the normal would always point directly at the camera:<br>
<img src="https://i.imgur.com/S2Qy4cc.png" alt=""></p>
<p>Now besides this normal there are also rotation values: Roll, Yaw and Pitch. The rendered sprite is not only positioned by the orientation of the normal vector, but can also “tilt” in any direction, as if the normal would be titled. This effect stacks with the rotation of the normal. So in which way does my sprite rotate, when I change these values?</p>
<p>This answer is not obvious at all. Because that might depend on what you’re currently rendering and with which Operator you try to change these values.</p>
<h2 id="sprite-rotation">Sprite Rotation</h2>
<p>Let’s start with the rotation of sprites. First of all, sprites normally ignore the normal, unless the orientation type is set to <code>Particle Normal Align</code> or <code>Screen &amp; Particle Normal Align</code>. So we ignore that for now and start with the most common one: <code>Screen Align</code>.</p>
<p>To rotate the sprite, we start by using the <code>Rotation random</code> Initializer. Here we can set the degrees we want to rotate and the rotation field:</p>
<p><em>Note: For better visualization, continuously spinning sprites were used. That is not the case with using ‘Rotation Random’.</em></p>
<ul>
<li><code>Roll</code>: rotates the sprite around its <code>Z</code>-axis. So in this case our normal.<br>
<img src="https://i.imgur.com/3TXyUzR.gif" alt=""></li>
<li><code>Roll Speed</code>: same as roll, but instead of a one-time rotation it keeps a spinning speed.</li>
<li><code>Yaw</code>: rotates the sprite around the <code>X</code>-axis.<br>
<img src="https://i.imgur.com/aOhP64a.gif" alt=""></li>
<li><code>Pitch</code>: does absolutly nothing. Can’t be used at all for sprites.</li>
</ul>
<p>Now we want to achieve a continuously spinning effect instead of a one-time rotation (like in gifs above). The normal way to do this, is the <code>Rotation speed random</code> Initializer. Like its counterpart without speed we can input degrees (this time per second) and a rotation field:</p>
<ul>
<li><code>Roll</code>, <code>Roll Speed</code>, <code>Yaw</code>, <code>Pitch</code>: rotates the sprite around the <code>Z</code>-axis.<br>
<img src="https://i.imgur.com/3TXyUzR.gif" alt=""><br>
So in this case it is completly irrelevant what field we choose.</li>
</ul>
<p>Now how can we spin the particle around other axis? Additionally to the Initializers we also have different kinds of Operators.</p>
<ul>
<li><code>Rotation spin roll</code> does the same as <code>Rotation speed random</code> above.</li>
<li><code>Rotation spin yaw</code> however, spins our sprite around the <code>X</code>-axis.</li>
</ul>
<p><em>Note: We can also use direct value manipulation like ‘Ramp scalar linear random’ to ramp up the yaw/roll value.</em></p>
<p>The same applies to other orientation types, like <code>World-Z Align</code>:</p>
<ul>
<li>Roll:<br>
<img src="https://i.imgur.com/m6Ry5Na.gif" alt=""></li>
<li>Yaw:<br>
<img src="https://i.imgur.com/e07FdRf.gif" alt=""></li>
</ul>
<p><strong>Conclusion:</strong><br>
Roll: rotates around the <code>Z</code>-axis.<br>
Yaw: rotates around the <code>X</code>-axis.<br>
Pitch: not available.</p>
<h2 id="model-rotation">Model Rotation</h2>
<p>Now we’ll have a look at the rotation of models. On models we have some additional options, but also some changes. So whatever applied to sprites might be completly different here.</p>
<h3 id="standard-orientation">Standard Orientation:</h3>
<p>If we simply render a model and change no properties of the renderer, we get something like that:<br>
<img src="https://i.imgur.com/5D9b7MK.png" alt=""><br>
We can see that the coloring of the axes from the grid is different than the ones on the model. If we want to change this, we have two options:</p>
<ul>
<li>
<p>check <code>ignore normal</code>:<br>
<img src="https://i.imgur.com/lJjo1JU.png" alt=""><br>
which corrects our <code>Z</code>-axis, but swaps <code>X</code> and <code>Y</code>.</p>
</li>
<li>
<p>check <code>orient model z to normal</code> (uncheck <code>ignore normal</code>):<br>
<img src="https://i.imgur.com/4WB0I8c.png" alt=""><br>
With this option enabled, we get a matching color coding. So keep this option enabled for the rest of the guide.</p>
</li>
</ul>
<p>We start as with sprites with the <code>Rotation random</code> Initializer:</p>
<p><em>Note: For better visualization, continuously spinning models were used. That is not the case with using ‘Rotation Random’.</em></p>
<ul>
<li><code>Roll</code>: rotates around the <code>Y</code>-axis.<br>
<img src="https://i.imgur.com/so8aAIm.gif" alt=""></li>
<li><code>Roll speed</code>: same as roll, but instead of a one-time rotation it keeps a spinning speed.</li>
<li><code>Yaw</code>: rotates around the <code>Z</code>-axis.<br>
<img src="https://i.imgur.com/M0LQkWW.gif" alt=""></li>
<li><code>Pitch</code>: rotates around the <code>X</code>-axis.<br>
<img src="https://i.imgur.com/Qu1nCbu.gif" alt=""></li>
</ul>
<p>So this time every rotation field actually worked. However, the axes for the rotation are different than the sprite ones.</p>
<p>Now we want to achieve a continuously spinning effect. Starting with <code>Rotation speed random</code>:</p>
<ul>
<li><code>Roll</code>, <code>Roll Speed</code>, <code>Yaw</code>, <code>Pitch</code>: rotates the sprite around the <code>Y</code>-axis:<br>
<img src="https://i.imgur.com/so8aAIm.gif" alt=""><br>
As in sprites, this Initializer can only achieve a “roll” effect.</li>
</ul>
<p>Now regarding Operators:</p>
<ul>
<li><code>Rotation spin roll</code> does the same as <code>Rotation speed random</code> above.</li>
<li><code>Rotation spin yaw</code> however, spins our sprite around the <code>Y</code>-axis.</li>
</ul>
<p>Since pitch is actually working on models, we need to find a way to rotate a models around the <code>X</code>-axis. Here we’re forced to directly manipulate the pitch value. Best way to do so, would be with the Operator <code>Ramp scalar linear simple</code> or <code>Ramp scalar linear random</code> and choose <code>Pitch</code> as the <code>ramp field</code>. This does also work for roll and yaw.</p>
<p>Besides that we can also use the particle normal to rotate our model. For that we’re using the <code>Rotate vector random</code> Operator. There we can enter a rotation rate and the axis we want to spin around. So we can do the following:</p>
<ul>
<li><code>Roll</code>: Use <code>0 1 0</code> as the spinning axis.</li>
<li><code>Pitch</code>: Use <code>1 0 0</code> as the spinning axis.</li>
<li><code>Yaw</code>: we can’t use <code>0 0 1</code> alone, becasue that doesn’t change the direction of the normal. But it can be used together with the others</li>
</ul>
<p><strong>Conclusion:</strong><br>
Roll: rotates around the <code>Y</code>-axis.<br>
Yaw: rotates around the <code>Z</code>-axis.<br>
Pitch: rotates around the <code>X</code>-axis.</p>

