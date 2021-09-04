<p>back to the <a href="../Tutorials.md">Tutorials</a>.</p>
<h1 id="particle-destruction">Particle Destruction</h1>
<p>If you ever worked with particles before, you probably saw “<em>Endcap</em>” or “<em>Decay</em>” somewhere before. But what is that and what does it do?<br>
In this tutorial I want to answer most questions about <strong>Particle Death</strong> and why its very important to keep track of.</p>
<h2 id="particle-count">Particle Count</h2>
<p>Whener you create a new particle, it needs resources and uses those until it is destroyed. So to keep the performance of you particle as high as possible, its very important to keep track of how many particles you create and maintain.<br>
On the top left corner of your particle renderer, numbers will show you the exact count of particles in your current system, or the sum together with all childs:<br>
<img src="https://i.imgur.com/VNIYqZR.png" alt=""></p>
<h3 id="max-particles">Max particles</h3>
<p>You can set the maximum amount of allowed particles under <em>Base Properties</em>. You should always try to keep it as low as possible. If you create a particle effect, leave it as its default 1000 at first and adjust it accordingly to the highest particle count you ever reached.</p>
<h2 id="killing-particles">Killing Particles</h2>
<p>Particles won’t simply die, if there isn’t any reason to do so. There are generally 3 ways to kill particles:</p>
<ul>
<li><a href="#Decay">Decay</a> - killing particles based on their attributes</li>
<li><a href="Explicit-Destruction">Explicit Destruction</a> -  killing particles with special operators</li>
<li>Destruction through code</li>
</ul>
<h2 id="decay">Decay</h2>
<p>Decay is the most common form of destroying particles. Even if you want to kill your particles another way, its best practice to <strong>always</strong> add a decay operator. If you don’t have any decay operator this warning message will show up until you added one:<br>
<img src="https://i.imgur.com/IWyHulD.png" alt=""></p>
<h3 id="how-decay-works">How decay works</h3>
<p>In general decay operators check specific attributes of particles every tick and then decide whether the particle should die or not.<br>
E.g. if you use <em>Lifespan Decay</em>, this operator will check if the lifespan of the particle exceeds the lifetime. If that’s the case, it will die.<br>
Often you can also use more than one decay type at once and they will kill particles if any of their conditions are true.</p>
<h3 id="decay-types">Decay types</h3>
<p>You can find all decay operators if you simply search for “decay” while adding an operator. I will cover them here:</p>
<ul>
<li><strong>Lifespan Decay</strong> -  most used decay operator that kills the particle, if the lifespan exceeds the lifetime.</li>
<li><strong>Lifespan minimum alpha decay</strong> - kills the particle, if the alpha value falls below the <em>minimum alpha</em> value.</li>
<li><strong>Lifespan minimum radius decay</strong> - kills the particle, of the radius value falls below the <em>minumum radius</em>value.</li>
<li><strong>Lifespan minimum velocity decay</strong> -  kills the particle, if the current velocity is lower than the <em>minimum velocity</em> value.</li>
<li><strong>Alpha Fade and Decay</strong> - simply a combination of <em>Lifespan Decay</em>, <em>Alpha Fade In Simple</em> and <em>Alpha Fade Out Simple</em>.</li>
<li><strong>Lifespan clamp count decay</strong> - kills the oldest particle, if the new particle would exceed the set <em>Maximum Count</em> value.</li>
<li><strong>Lifespan endcap timed decay</strong> - special decay operator,  more explanation <a href="#Endcap">later</a>.</li>
<li><strong>Other</strong> - all other decay operators are rarely ever used or can be broken or not working anymore.</li>
</ul>
<h2 id="explicit-destruction">Explicit Destruction</h2>
<p>Besides decay you can kill particles with other means too. I will explain some of them here:</p>
<h4 id="stop-effect-after-duration">Stop effect after duration</h4>
<p>This pre-emission operator will destroy all particles after a specified duration. This duration can also be set to any control point value. This operator will also kill all child particles.<br>
You can also choose if you want endcap effects to play or not.</p>
<h4 id="cull-when-crossing-sphere">Cull When Crossing Sphere</h4>
<p>This operator will kill all particles, that are outside a specified sphere. It can also be inversed so that only particles inside the sphere get killed.</p>
<h4 id="cull-when-crossing-plane">Cull When Crossing Plane</h4>
<p>Same as the operator above, but with a plane instead of a sphere.</p>
<h4 id="cull-relative-to-model">Cull relative to model</h4>
<p>Similar to the operators above, but it uses the hitbox of models instead of spheres or planes.</p>
<h4 id="cull-random">Cull random</h4>
<p>Randomly kills particles with a certain percentage.</p>
<h2 id="endcap">Endcap</h2>
<p>Endcap is a special state that is entered once a particle system is destroyed. This will never occur, if you simply kill particles wither through decay or Culls, since that only kills single particles, rather than the whole system.</p>
<p>A particle system typically only gets killed through code. When you use <code>DestroyParticleEffect</code> or similar methods, this will destroy the complete particle system.</p>
<p><strong>Important:</strong> Killing a particle system does <strong>not</strong> automatically kill all particles.</p>
<p>Once a particle system is destroyed, it can’t be controlled any longer and will remain in its endcap state forever. If the system is in that state AND there are no particles anymore (and for its childs as well), it will be removed completely and does not take any resources any longer. That’s the reason you always need a decay operator, otherwise the particle systems resourced will never be cleared again.</p>
<p>You can choose the active state for all operators seperately to be either: <em>Always enabled</em>, <em>Disabled During Endcap</em> or <em>Only Endabled During Endcap</em>.</p>
<h3 id="endcap-decay">Endcap decay</h3>
<p>If you only want to destroy your particles once the endcap state is reached, you have multiple options. The easiest one is to use the (priviously mentioned) operator <strong>Lifespan endcap timed decay</strong>. This operator will kill all particles after a delay based on the <em>decay time</em> after the endcap state was reached.<br>
Besides that it’s also possible to simply use the <em>Only Endabled During Endcap</em> option.</p>
<h3 id="endcap-actions">Endcap actions</h3>
<p>Generally speaking you could let your particle do anything in the endcap state with using the <em>Only Endabled During Endcap</em> option.<br>
However there are operators that only work on endcap by default:</p>
<ul>
<li><strong>Lerp endcap scalar</strong> - Smoothly scales a particle attribute to the desired outcome over a specified duration. Often used for radius or alpha fading out in the endcap state.</li>
<li><strong>Lerp endcap vector</strong> -  Same as above but for vector attributes. Probably mostly used for color.</li>
<li><em>Many others…</em></li>
</ul>
<h3 id="endcap-childs">Endcap childs</h3>
<p>You have to options to only fire child particles, once you reach the endcap state. To do this simply check <em>end cap effect</em> for the child effect.<br>
This is often used for explosion effects on projectiles, since their endcap will fire automatically once they are destroyed (distance reached, etc).</p>
<h3 id="triggering-endcaps">Triggering Endcaps</h3>
<p>Besides the trigger from killing the system from code, there are two other options you have:</p>
<ul>
<li><strong>Stop effect after duration</strong> - This will also destroy the current particles system and not only its particles, so it also enters the endcap state. If <em>destroy all particles immediatly</em> is checked, all particles will be destroyed regardless of their endcap decay (e.g. set through <em>Lifespan endcap timed decay</em>). This will still trigger endcap child effects.</li>
<li><strong>Play EndCap when Finished</strong> -  This pre emission operator will set the state to endcap state, once all particles are dead (normally it would not change to endcap state this way). Also there is an option to directly go into endcap state once all particles are emitted.</li>
</ul>

