---


---

<p>back to the <a href="../Tutorials.md">Tutorials</a>.</p>
<h1 id="linear-projectiles">Linear Projectiles</h1>
<h2 id="maintain-launch-offset">1. Maintain Launch Offset</h2>
<p>What is the problem? Linear projectiles often maintain a set distance to the ground, which can result in unwanted effects. If you want to launch your projectile from a specific height, it should also stay in this relative position to the ground.</p>
<p>We’re about to heavily modify your particle effect. So if you want, make a backup of it as a security measure.</p>
<h3 id="step-1-creating-a-parent-dummy-particle">Step 1: Creating a parent dummy particle</h3>
<p>There’s only one way to change this relative ground offset dynamically, which is scaling it with the particle radius. But since we don’t want to actually touch the radius of our projectile particle, we create a new one, to perform this task.</p>
<p>So first create a new particle and save it somewhere you like. If the linear projectile particle is already saved somewhere, save this one in the same position. Next we need some basic stuff before we can move the important ones over.</p>
<p>First we need an Initializer and <code>Emit instantaneously</code> is all we need. Since this is going to be only a control particle we can set the amount to 1. The other basic thing we need is a <code>Lifespan decay</code> to get rid of the warning you should see in the bottom left. set it’s <code>end cap state</code> to 1, so it’s unaffected by <code>lifetime</code>. Thus, we should not forget <code>Position within sphere random</code> to emit our particle at the right location.</p>
<h3 id="step-2-copy-the-behavior">Step 2: Copy the behavior</h3>
<p>Now we need to get all the functions from our original projectile particle effect. Mark the following functions</p>
<ul>
<li><code>Velocity set from control point</code></li>
<li><code>Movement basic</code></li>
<li><code>Set control points from particle positions</code></li>
<li><code>Movement place on ground</code></li>
</ul>
<p>and cut them with Ctrl + X. Go back to your new particle and paste them in with Ctrl + V. To try it out, you can also add a <code>Render sprites</code> to see if your new effect is working as intended.</p>
<h3 id="step-3-adjust-the-behavior">Step 3: Adjust the behavior</h3>
<p>Next, we need to actually make the ground offset scale with the launch offset. To do so go to your <code>Movement place on ground</code> function and change it’s <code>offset</code> to 1. Now also check <code>treat offset as scalar of particle radius</code>. Leave all other fields as they were.</p>
<p>The next step is to let the radius of this particle scale with our z-offset. So we need to add <code>Remap control point to scalar</code> as an Initializer. Set it’s input field to <code>Z Component</code>. Also set <code>input maximum</code> and <code>output maximim</code> to a high number like 10000. Otherwise, it would always be stuck at 1.</p>
<p>If you try to change the z-offset now, you should see that the offset is changed and maintained. But also that the sprite is massive. Once you make sure everything’s working, disable <code>Render sprites</code>.</p>
<h3 id="step-4-fix-our-original-particle-effect">Step 4: Fix our original particle effect</h3>
<p>Now we can add our original effect as a child to our placeholder. After that go back to your original. We’ve already removed all the parts we don’t need for this one anymore. But we also need some new stuff to make it work properly again.</p>
<p>To achieve this, just add <code>Movement lock to control point</code> as an Operator and set it’s <code>control point number</code> to 3. It should now follow our invisible dummy particle.</p>
<p>So if you want to use your new linear projectile particle, make sure to always use the newly created particle effect and not the original one!</p>

