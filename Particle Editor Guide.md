---


---

<h1 id="particle-editor-guide">Particle Editor Guide</h1>
<h2 id="contents">Contents</h2>
<ul>
<li><a href="#the-tool">The Tool</a>
<ul>
<li><a href="#menu">Menu</a></li>
<li><a href="#preview">Preview</a></li>
<li><a href="#functions">Functions</a></li>
<li><a href="#properties">Properties</a></li>
<li><a href="#controls">Controls</a></li>
</ul>
</li>
<li><a href="#functions-1">Functions</a>
<ul>
<li><a href="#base-properties">Base Properties</a></li>
<li><a href="#emitter">Emitter</a></li>
</ul>
</li>
</ul>
<h2 id="the-tool">The Tool</h2>
<p>(<a href="https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Particles/Particle_Editor">Valves official documentation of the Tool</a>)</p>
<p>There are two ways to open the Particle Editor: The first is to click on the flame symbol on the top left of the main asset browser window to open a blank new window. The second way is to directly open an existing particle effect by double clicking it in the asset browser.</p>
<p>Now open an existing particle effect as an example:</p>
<h3 id="menu">Menu</h3>
<p>In the top left you have standard menu actions with File, Edit, View and Help. There’s nothing special about it and just some default operations like save, open etc.<br>
Important note here: In order to modify valves particles you need to save it in your current addon.</p>
<h3 id="preview">Preview</h3>
<p>The biggest part of your window should be filled with a preview part in the middle. There you can already see how the effect will eventually look like in the game. You can move freely with WASD, the right mouse button and the mouse wheel to see the effect from any side and distance. In the top left are two lines of text that display statistics of the number of particles.<br>
The icons in the top bar mainly handle the playback of the effect in the preview window. Here you can stop the simulation, restart it, etc.<br>
<img src="https://i.imgur.com/ktpuMb6.png" alt="alt text"><br>
To the right there are two more buttons that can be used to reset the camera, e.g. if you have navigated the camera unfavorably.<br>
<img src="https://i.imgur.com/jMP5TY3.png" alt="alt text"><br>
The last button in the row is the most important one: Visualize allows you to graphically display various, otherwise invisible, attributes. It opens a small extra window where you can choose what you want to display.<br>
<img src="https://i.imgur.com/Mj7G1HC.png" alt="alt text"><br>
Most important is the first item <code>Visualize Attributes</code> which allows you to display specific attributes like radius, alpha etc. Also, <code>Show Control Points</code> which shows all currently active control points. If there is too much information, disable <code>Include Child Systems</code> to ignore the child effect data.</p>
<h3 id="functions">Functions</h3>
<p>The functions are the heart of every particle effect. Here you can define all properties and behaviors that make the effect what it is. In the upper part, there are also 4 small buttons that make navigation much easier.</p>
<p><img src="https://i.imgur.com/XppFQIR.png" alt="alt text"></p>
<p>If you have more than one effect open at the same time in the particle editor, you can jump to the last displayed effect with the left arrow. Likewise, the arrow to the right leads to the next effect. The button to the right is either grayed out and shows a P or a number. If the current effect is added to another effect as a child you can use it to display a list of these effects and jump to them. Vice versa the button next to it with a number or a capital C. This shows subordinate effects in a tree structure. If these two buttons are not clickable, it means that there are no effects available at the moment.<br>
More about the functions in detail here: <a href="#Functions-1">Functions</a>.</p>
<h3 id="properties">Properties</h3>
<p>The detailed data for the currently selected function is displayed here. If you want to make changes to one of the functions, this is the right place to do so.</p>
<h3 id="controls">Controls</h3>
<p>The control part is divided into two parts: the control points and preview. Control points are 3-dimensional vectors that form the interface between the particle effect and the code.<br>
<img src="https://i.imgur.com/1OU3mSS.png" alt="alt text"><br>
By clicking on the colored icon to the right of the arrow, you can directly influence these points, for example by moving or rotating them. Alternatively you can also enter your desired values in the fields next to it. On the far right you will find a small lock symbol. If it is closed, the entered values are saved, so that the next time you open this effect in the Particle Editor, the values are immediately restored to the saved values. With the preview part below, other assets like models can be loaded directly into the current effect. This is only a test tool and has no influence on the final result displayed in the game. Nevertheless, it is essential for quick testing of different effects.</p>
<h2 id="functions-1">Functions</h2>
<p>Now that you have learned the general handling of the tool, we can start to take a closer look at the functions that make every effect work. Functions are divided into different groups, that will be explained here. You can find a complete list of all functions with their usage here: <a href="#Library">Functions Library</a><br>
To add a function to one of these groups, just click the plus icon and choose an element from the list.</p>
<h3 id="base-properties">Base Properties</h3>
<p>The base properties hold every information about the effect, including all other groups. In addition, both initial and other important values can be found here. Some initial values that can be set here are:</p>
<ul>
<li><code>color</code></li>
<li><code>radis</code></li>
<li><code>lifetime</code></li>
<li>others</li>
</ul>
<p>One of the most important fields here is <code>max particles</code> which is a hard cap to the number of particles maximal allowed for this effect (excluding child effects).</p>
<h3 id="emitter">Emitter</h3>
<p>Emitters are functions that can generate particles. They can therefore be found in almost every effect. Normally it is sufficient to use a kind of emitter. The most commonly used emitters among them are:</p>
<ul>
<li><code>Emit continuously</code> - emits particles in a set interval. <code>emission rate</code> is the count of particles emitted per second, <code>emission duration</code> is the duration in which particles are emitted and <code>emission start time</code> is a delay to the start of the emission in seconds. (<a href="#Library">Library</a>)</li>
<li><code>Emit instantaneously</code> - emits <code>num to emit</code> particles directly at the start of the effect all at once. The emission can be delayed with <code>emission start time</code>. (<a href="#Library">Library</a>)</li>
</ul>
<h3 id="initializer">Initializer</h3>
<h2 id="library">Library</h2>

