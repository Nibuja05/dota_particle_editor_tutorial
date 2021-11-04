<p>back to the <a href="../Tutorials.md">Tutorials</a>.</p>
<h1 id="introduction">Introduction</h1>
<p>Converting linear and tracking projectiles are problems encountered quite frequently.<br>
This tutorial will guide you through that process.</p>
<h2 id="foreword-projectiles">Foreword: Projectiles</h2>
<p>Linear and tracking projectiles are not that different in their structure and have many similarities:</p>
<ul>
<li><strong>CP0</strong>: start point of the projectile</li>
<li><strong>CP3</strong>: current position of the projectile (used for child effects)</li>
</ul>
<p>Additionally linear projectiles use <strong>CP1</strong> for the velocity.<br>
Respectively tracking projectiles use <strong>CP1</strong> as target point and <strong>CP2.x</strong> as maximum speed.</p>
<p>Since the children are often the main part of projectile particles, we can resuse most of it without any changes needed.</p>
<h1 id="tracking-projectile---linear-projectile">Tracking Projectile -&gt; Linear Projectile</h1>
<h2 id="quick-start">Quick start</h2>
<p>Open your tracking projectile particle in the Particle Editor. Now select all its children (by pressing <em>Ctrl</em>) and then copy them (by pressing <em>Ctrl + C</em>).</p>
<p>Now go back to the asset browser and search for <code>particles/dev/library/base_linear_projectile_model.vpcf</code>. Open this particle in the Particle Editor. Now paste in all the children (by pressing <em>Ctrl + V</em>). You should also disable the <code>Render models</code> renderer, by clicking on the checkmark icon on its left.</p>
<p>Save this particle under your name (by pressing <em>Ctrl + Shift + S</em>). You can now use this as a fully functional linear projectile.</p>
<h2 id="further-improvements">Further improvements</h2>
<p>While we copied all the child effects, the projectile particle itself might have also had an effect. Go back to your original tracking projectile and check if there are any active Renderers (checkmark active).</p>
<p>If there aren’t any active Renderer, you are done!</p>
<p>If there are, we probably also want to copy them. TO do so, follow these steps:</p>
<h3 id="prepare-the-linear-projectile">Prepare the linear projectile</h3>
<ul>
<li>Go to your new linear projectile.</li>
<li>Delete all Emitters</li>
<li>Delete all Initializer that are not named <code>Normal align to CP</code> or <code>Velocity set from control point</code></li>
<li>Delete all Operators that are not <code>Movement basic</code>, <code>Lifespan decay</code>, <code>Set control points from particle positions</code>,  <code>Movement place on ground</code> or <code>Remap velocity to vector</code>.</li>
<li>Delete all Renderer</li>
</ul>
<h3 id="copy-the-important-stuff">Copy the important stuff</h3>
<ul>
<li>Go to your original tracking projecitle</li>
<li>Select all Emitters</li>
<li>Select all Initializers</li>
<li>Select all Operators, except <code>Movement Basic</code>, <code>Movement max velocity</code>, <code>Rotation orient relative to CP</code>, <code>Set control points from particle positions</code>, <code>Set CP offset to CP percentage between two control points</code> and <code>Remap velocity to vector</code></li>
<li>Select all Renderer</li>
<li>Copy the selected parts to your new linear projectile</li>
</ul>
<h3 id="finishing">Finishing</h3>
<p>All thats left is to match the base properties. If you go back to your original tracking projectile you can click on <code>Base Properties</code> at the very top. If you do, you probably see some field names marked in blue: This means these values are changed and not default.<br>
Now you can copy the <code>Base Properties</code> to your new linear projectile like you did with all other operators.</p>
<p>You now completly replicated your tracking particle as a linear one. Well done!</p>
<h1 id="linear-projectile---tracking-projectile">Linear Projectile -&gt; Tracking Projectile</h1>
<p>The same as <a href="#linear">Tracking Projectile -&gt; Linear Projectile</a>, but reversed.</p>
<p><em>Detailed Tutorial coming soon</em>…</p>

