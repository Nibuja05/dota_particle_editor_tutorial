---


---

<p>back to the <a href="README.md">Overview</a>.</p>
<h1 id="function-library">Function Library</h1>
<p>A collection of all (the most) functions available and information about them. This data is auto-generated from different sources, so the data provided may not be 100% accurate.</p>
<h2 id="contents">Contents</h2>
<ul>
<li><a href="#operator">Operator</a>
<ul>
<li><a href="#lifespan-decay">Lifespan decay</a></li>
<li><a href="#radius-scale">Radius scale</a></li>
<li><a href="#movement-basic">Movement basic</a></li>
<li><a href="#alpha-fade-out-simple">Alpha fade out simple</a></li>
<li><a href="#alpha-fade-in-simple">Alpha fade in simple</a></li>
<li><a href="#color-fade">Color fade</a></li>
<li><a href="#movement-lock-to-control-point">Movement lock to control point</a></li>
<li><a href="#ramp-scalar-linear-simple">Ramp scalar linear simple</a></li>
<li><a href="#rotation-basic">Rotation basic</a></li>
<li><a href="#noise-vector">Noise vector</a></li>
<li><a href="#oscillate-vector">Oscillate vector</a></li>
<li><a href="#ramp-scalar-linear-random">Ramp scalar linear random</a></li>
<li><a href="#lifespan-endcap-timed-decay">Lifespan endcap timed decay</a></li>
<li><a href="#lerp-endcap-scalar">Lerp endcap scalar</a></li>
<li><a href="#alpha-fade-and-decay">Alpha fade and decay</a></li>
<li><a href="#movement-lock-to-bone">Movement lock to bone</a></li>
<li><a href="#oscillate-scalar">Oscillate scalar</a></li>
<li><a href="#alpha-fade-out-random">Alpha fade out random</a></li>
<li><a href="#remap-distance-to-control-point-to-scalar">Remap distance to control point to scalar</a></li>
<li><a href="#movement-skin-to-bones-rigid">Movement skin to bones rigid</a></li>
<li><a href="#inherit-attribute-from-parent-particle">Inherit attribute from parent particle</a></li>
<li><a href="#noise-scalar">Noise scalar</a></li>
<li><a href="#rotation-spin-roll">Rotation spin roll</a></li>
<li><a href="#movement-rotate-particle-around-axis">Movement rotate particle around axis</a></li>
<li><a href="#alpha-fade-in-random">Alpha fade in random</a></li>
<li><a href="#lifespan-minimum-alpha-decay">Lifespan minimum alpha decay</a></li>
<li><a href="#rotation-orient-relative-to-cp">Rotation orient relative to CP</a></li>
<li><a href="#ramp-scalar-spline-random">Ramp scalar spline random</a></li>
<li><a href="#movement-dampen-relative-to-control-point">Movement dampen relative to control point</a></li>
<li><a href="#movement-max-velocity">Movement max velocity</a></li>
<li><a href="#clamp-scalar">Clamp scalar</a></li>
<li><a href="#movement-set-to-control-point">Movement set to control point</a></li>
<li><a href="#oscillate-scalar-simple">Oscillate scalar simple</a></li>
<li><a href="#set-child-control-points-from-particle-positions">Set child control points from particle positions</a></li>
<li><a href="#cull-when-crossing-sphere">Cull when crossing sphere</a></li>
<li><a href="#movement-place-on-ground">Movement place on ground</a></li>
<li><a href="#set-control-points-from-particle-positions">Set control points from particle positions</a></li>
<li><a href="#set-per-child-control-point-from-particle-positions">Set per child control point from particle positions</a></li>
<li><a href="#lerp-initial-scalar">Lerp initial scalar</a></li>
<li><a href="#remap-speed-to-scalar">Remap speed to scalar</a></li>
<li><a href="#remap-control-point-to-scalar">Remap control point to scalar</a></li>
<li><a href="#remap-percentage-between-two-control-points-to-scalar-">Remap percentage between two control points to scalar </a></li>
<li><a href="#lifespan-minimum-radius-decay">Lifespan minimum radius decay</a></li>
<li><a href="#movement-maintain-positon-along-path">Movement maintain positon along path</a></li>
<li><a href="#set-float">Set Float</a></li>
<li><a href="#movement-skin-to-bones">Movement skin to bones</a></li>
<li><a href="#remap-direction-to-cp-to-vector">Remap direction to CP to vector</a></li>
<li><a href="#remap-control-point-to-vector">Remap control point to vector</a></li>
<li><a href="#movement-lock-to-saved-position-along-path">Movement lock to saved position along path</a></li>
<li><a href="#remap-velocity-to-vector">Remap velocity to vector</a></li>
<li><a href="#oscillate-vector-simple">Oscillate vector simple</a></li>
<li><a href="#ramp-scalar-spline-simple">Ramp scalar spline simple</a></li>
<li><a href="#inherit-attribute-from-parent-particle-1">Inherit attribute from parent particle</a></li>
<li><a href="#rotate-vector-random">Rotate vector random</a></li>
<li><a href="#movement-lerp-to-hitbox">Movement lerp to hitbox</a></li>
<li><a href="#remap-control-point-direction-to-vector">Remap control point direction to vector</a></li>
<li><a href="#rotation-orient-to-2d-direction">Rotation orient to 2d direction</a></li>
<li><a href="#color-fade-random">Color fade random</a></li>
<li><a href="#remap-scalar">Remap scalar</a></li>
<li><a href="#color-light-from-control-point">Color light from control point</a></li>
<li><a href="#set-cp-offset-to-cp-percentage-between-two-control-points">Set CP offset to CP percentage between two control points</a></li>
<li><a href="#rotation-from-cp-forward-orientation">Rotation from CP forward orientation</a></li>
<li><a href="#remap-cp-orientaton-to-rotations">Remap CP orientaton to rotations</a></li>
<li><a href="#lerp-endcap-vector">Lerp endcap vector</a></li>
<li><a href="#normalize-vector">Normalize vector</a></li>
<li><a href="#remap-distance-between-two-control-points-to-scalar">Remap distance between two control points to scalar</a></li>
<li><a href="#remap-distance-between-two-control-points-to-scalar-1">Remap distance between two control points to scalar</a></li>
<li><a href="#remap-game-visibility-scalar">Remap game visibility scalar</a></li>
<li><a href="#movement-loop-inside-sphere">Movement loop inside sphere</a></li>
<li><a href="#remap-particle-count-on-endcap-scalar">Remap particle count on endcap scalar</a></li>
<li><a href="#clamp-vector">Clamp vector</a></li>
<li><a href="#movement-match-particle-velocities">Movement match particle velocities</a></li>
<li><a href="#restart-effect-after-duration">Restart effect after duration</a></li>
<li><a href="#remap-game-visibility-of-cp-to-scalar-">Remap game visibility of CP to scalar </a></li>
<li><a href="#remap-difference-of-sequential-particle-vector-to-scalar">Remap difference of sequential particle vector to Scalar</a></li>
<li><a href="#remap-particle-count-to-scalar">Remap particle count to scalar</a></li>
<li><a href="#movement-maintain-offset">Movement maintain offset</a></li>
<li><a href="#set-cp-orientation-to-cp-direction">Set CP orientation to CP direction</a></li>
<li><a href="#cull-when-crossing-plane">Cull when crossing plane</a></li>
<li><a href="#remap-percentage-between-two-control-points-to-vector">Remap percentage between two control points to vector</a></li>
<li><a href="#remap-scalar-once-timed">Remap scalar once timed</a></li>
<li><a href="#cycle-scalar">Cycle Scalar</a></li>
<li><a href="#lifespan-from-endcap-decay">Lifespan from endcap decay</a></li>
<li><a href="#remap-vector-to-cp">Remap vector to CP</a></li>
<li><a href="#set-vec">Set Vec</a></li>
<li><a href="#lerp-initial-vector">Lerp initial vector</a></li>
<li><a href="#set-cp-orientation-to-ground-normal">Set CP orientation to ground normal</a></li>
<li><a href="#pin-particle-to-control-point">Pin Particle to control point</a></li>
<li><a href="#remap-dot-product-to-scalar">Remap dot product to scalar</a></li>
<li><a href="#movement-lock-to-saved-position-along-path-1">Movement lock to saved position along path</a></li>
<li><a href="#lifespan-maintain-count-decay-">Lifespan maintain count decay </a></li>
<li><a href="#reinitalize-on-endcap-scalar-random">Reinitalize on endcap scalar random</a></li>
<li><a href="#remap-cp-velocity-to-vector">Remap CP velocity to vector</a></li>
<li><a href="#set-vector-from-control-point">Set vector from control point</a></li>
<li><a href="#movement-lerp-to-initial-position-relative-to-cp">Movement Lerp to Initial Position relative to CP</a></li>
<li><a href="#calculate-vector-attribute">Calculate vector attribute</a></li>
<li><a href="#remap-on-endcap-scalar-">Remap on endcap scalar </a></li>
<li><a href="#remap-distance-to-line-between-2-control-points-to-vector">Remap distance to line between 2 control points to vector</a></li>
<li><a href="#remap-control-point-orientaton-to-rotation">Remap control point orientaton to rotation</a></li>
<li><a href="#remap-distance-to-line-between-2-control-points-to-scalar">Remap distance to line between 2 control points to scalar</a></li>
<li><a href="#remap-percentage-between-two-cps-to-lerp-cps-to-scalar">Remap percentage between two cps to lerp CPs to scalar</a></li>
<li><a href="#remap-control-point-to-velocity">Remap control point to velocity</a></li>
<li><a href="#point-vector-at-next-particle-position">Point vector at next particle position</a></li>
</ul>
</li>
<li><a href="#init">Init</a>
<ul>
<li><a href="#lifetime-random">Lifetime random</a></li>
<li><a href="#radius-random">Radius Random</a></li>
<li><a href="#rotation-random">Rotation random</a></li>
<li><a href="#color-random">Color Random</a></li>
<li><a href="#position-within-sphere-random">Position within sphere random</a></li>
<li><a href="#alpha-random">Alpha Random</a></li>
<li><a href="#position-modify-offset-random">Position modify offset random</a></li>
<li><a href="#sequence-random">Sequence Random</a></li>
<li><a href="#velocity-noise">Velocity noise</a></li>
<li><a href="#rotation-yaw-flip-random">Rotation yaw flip random</a></li>
<li><a href="#remap-particle-count-to-scalar-1">Remap particle count to scalar</a></li>
<li><a href="#rotation-speed-random">Rotation speed random</a></li>
<li><a href="#position-along-ring">Position along ring</a></li>
<li><a href="#remap-scalar-1">Remap scalar</a></li>
<li><a href="#trail-length-random">Trail length random</a></li>
<li><a href="#remap-control-point-to-scalar-1">Remap control point to scalar</a></li>
<li><a href="#position-from-parent-particles">Position from parent particles</a></li>
<li><a href="#position-modify-place-on-ground">Position modify place on ground</a></li>
<li><a href="#position-skin-to-bones-from-cp-snapshot">Position skin to bones from CP snapshot</a></li>
<li><a href="#rotation-yaw-random">Rotation yaw random</a></li>
<li><a href="#remap-noise-to-scalar">Remap noise to scalar</a></li>
<li><a href="#inherit-attribute-from-parent-particle-2">Inherit attribute from parent particle</a></li>
<li><a href="#position-modify-warp-random">Position modify warp random</a></li>
<li><a href="#velocity-random">Velocity random</a></li>
<li><a href="#position-along-path-sequential">Position along path sequential</a></li>
<li><a href="#remap-control-point-to-vector-1">Remap control point to vector</a></li>
<li><a href="#scalar-random">Scalar random</a></li>
<li><a href="#init-from-cp-snapshot">Init from CP snapshot</a></li>
<li><a href="#normal-align-to-cp">Normal align to CP</a></li>
<li><a href="#sequence-two-random">Sequence two random</a></li>
<li><a href="#velocity-inherit-from-control-point">Velocity inherit from control point</a></li>
<li><a href="#offset-vector-to-vector">Offset vector to vector</a></li>
<li><a href="#remap-initial-distance-to-control-point-to-scalar">Remap initial distance to control point to scalar</a></li>
<li><a href="#position-along-epitrochoid">Position along epitrochoid</a></li>
<li><a href="#init-from-killed-parent-particle">Init from killed parent particle</a></li>
<li><a href="#normal-lock-to-control-point">Normal lock to control point</a></li>
<li><a href="#remap-cp-orientation-to-rotation">Remap CP orientation to rotation</a></li>
<li><a href="#position-within-box-random">Position within box random</a></li>
<li><a href="#normal-modify-offset-random">Normal modify offset random</a></li>
<li><a href="#lifetime-from-sequence">Lifetime from sequence</a></li>
<li><a href="#remap-initial-direction-to-cp-to-vector">Remap initial direction to CP to vector</a></li>
<li><a href="#init-float">Init Float</a></li>
<li><a href="#velocity-set-from-control-point">Velocity set from control point</a></li>
<li><a href="#rotation-spin-yaw">Rotation spin yaw</a></li>
<li><a href="#vector-component-random">Vector component random</a></li>
<li><a href="#rotation-orient-relative-to-cp-1">Rotation orient relative to CP</a></li>
<li><a href="#init-status-effect">Init Status Effect</a></li>
<li><a href="#remap-scalar-to-vector">Remap scalar to vector</a></li>
<li><a href="#vector-random">Vector random</a></li>
<li><a href="#position-along-path-random">Position along path random</a></li>
<li><a href="#position-along-path-sequential-1">Position along path sequential</a></li>
<li><a href="#position-on-spiral-sphere">Position on spiral sphere</a></li>
<li><a href="#remap-qangie-in-cp-to-rotations">Remap QAngIe in CP to rotations</a></li>
<li><a href="#radius-from-cp-object">Radius from CP object</a></li>
<li><a href="#globally-scale-initial-attributes">Globally Scale Initial Attributes</a></li>
<li><a href="#set-hitbox-to-closest-hitbox">Set hitbox to closest hitbox</a></li>
<li><a href="#sequence-from-control-point">Sequence from control point</a></li>
<li><a href="#position-from-parent-cache-">Position from parent cache </a></li>
<li><a href="#cull-relative-to-ray-trace-environment-">Cull relative to ray trace environment </a></li>
<li><a href="#position-from-control-points">Position from control points</a></li>
<li><a href="#init-cp-orientation-to-rotations">Init CP orientation to rotations</a></li>
<li><a href="#init-vec">Init Vec</a></li>
<li><a href="#add-vector-to-vector">Add vector to vector</a></li>
<li><a href="#velocity-radial-random">Velocity radial random</a></li>
<li><a href="#remap-speed-to-scalar-1">Remap speed to scalar</a></li>
<li><a href="#lifetime-from-time-to-impact">Lifetime from time to impact</a></li>
<li><a href="#velocity-repulse-from-world">Velocity repulse from world</a></li>
<li><a href="#alpha-window-threshold-random">Alpha window threshold random</a></li>
<li><a href="#position-with-phyllotaxis-distribution">Position with phyllotaxis distribution</a></li>
<li><a href="#velocity-away-from-hitbox-random">Velocity away from hitbox random</a></li>
<li><a href="#position-modify-offset-relative-to-control-point">Position modify offset relative to control point</a></li>
<li><a href="#velocity-from-normal-random">Velocity from normal random</a></li>
<li><a href="#remap-initial-game-visibility-to-scalar">Remap initial game visibility to scalar</a></li>
<li><a href="#color-lit-per-particle">Color lit per particle</a></li>
<li><a href="#init-vector-attribute-from-a-list-of-values">Init vector attribute from a list of values</a></li>
<li><a href="#move-particles-between-2-control-points">Move particles between 2 control points</a></li>
<li><a href="#position-modify-warp-from-scalar">Position modify warp from scalar</a></li>
</ul>
</li>
<li><a href="#renderer">Renderer</a>
<ul>
<li><a href="#render-sprites">Render sprites</a></li>
<li><a href="#render-rope">Render rope</a></li>
<li><a href="#render-sprite-trail">Render sprite trail</a></li>
<li><a href="#render-deferred-light">Render deferred light</a></li>
<li><a href="#render-projected">Render projected</a></li>
<li><a href="#render-status-effect">Render Status Effect</a></li>
<li><a href="#render-screen-shake">Render screen shake</a></li>
<li><a href="#render-blobs">Render blobs</a></li>
<li><a href="#render-sound">Render sound</a></li>
<li><a href="#render-tree-shake">Render Tree Shake</a></li>
<li><a href="#render-text">Render Text</a></li>
</ul>
</li>
<li><a href="#emitter">Emitter</a>
<ul>
<li><a href="#emit-continuously">Emit continuously</a></li>
<li><a href="#emit-instantaniously">Emit instantaniously</a></li>
<li><a href="#emit-noise">Emit noise</a></li>
<li><a href="#emit-to-maintain-count">Emit to maintain count</a></li>
</ul>
</li>
<li><a href="#force-gen">Force-Gen</a>
<ul>
<li><a href="#pull-towards-control-point">Pull towards control point</a></li>
<li><a href="#random-force">Random force</a></li>
<li><a href="#twist-around-axis">Twist around axis</a></li>
<li><a href="#curlnoise-force">CurlNoise force</a></li>
<li><a href="#turbulent-force">Turbulent force</a></li>
<li><a href="#external-wind-force">External Wind force</a></li>
<li><a href="#local-acceleraton-force">Local acceleraton force</a></li>
<li><a href="#time-varying-force">Time varying force</a></li>
<li><a href="#force-based-on-distance-from-plane">Force based on distance from plane</a></li>
<li><a href="#create-vortices-from-parent-particles">Create vortices from parent particles</a></li>
</ul>
</li>
<li><a href="#pre">Pre</a>
<ul>
<li><a href="#set-single-control-point-position">Set single control point position</a></li>
<li><a href="#set-control-point-orientaton">Set control point orientaton</a></li>
<li><a href="#set-control-point-positions">Set control point Positions</a></li>
<li><a href="#set-per-child-control-point-from-parent-control-points">Set per child control point from parent control points</a></li>
<li><a href="#remap-cp-speed-to-cp">Remap CP speed to CP</a></li>
<li><a href="#hsv-shift-to-control-point">HSV Shift to control point</a></li>
<li><a href="#stop-effect-after-duraton">Stop effect after duraton</a></li>
<li><a href="#set-control-point-from-cp-object-scale">Set control point from CP object scale</a></li>
<li><a href="#set-control-point-rotation">Set control point rotation</a></li>
<li><a href="#set-control-point-to-random-position">Set control point to random Position</a></li>
<li><a href="#set-cp-orientaton-to-point-at-second-cp">Set CP orientaton to point at second CP</a></li>
<li><a href="#remap-average-scalar-value-to-cp">Remap average scalar value to CP</a></li>
<li><a href="#remap-cp-component-to-cp-component">Remap CP component to CP component</a></li>
<li><a href="#set-control-point-to-impact-point">Set control point to impact point</a></li>
<li><a href="#force-control-point-in-pet">Force Control Point In Pet</a></li>
<li><a href="#enable-children-from-parent-particle-count">Enable children from parent particle count</a></li>
<li><a href="#repeatedly-trigger-child-group">Repeatedly Trigger Child Group</a></li>
<li><a href="#set-control-point-component-to-scalar-expression">Set control point component to scalar expression</a></li>
<li><a href="#ramp-control-point-linear-random">Ramp control point linear random</a></li>
<li><a href="#use-random-children-in-group">Use Random Children in Group</a></li>
<li><a href="#set-dest-cp-field-1-if-source-cp-is-in-water-">Set dest CP field 1 if source CP is in water </a></li>
</ul>
</li>
<li><a href="#constraint">Constraint</a>
<ul>
<li><a href="#constrain-distance-to-control-point">Constrain distance to control point</a></li>
<li><a href="#collision-via-traces">Collision via traces</a></li>
<li><a href="#prevent-passing-through-a-plane">Prevent passing through a plane</a></li>
<li><a href="#constrain-distance-to-path-between-two-control-points">Constrain distance to path between two control points</a></li>
<li><a href="#constrain-particles-to-a-box">Constrain particles to a box</a></li>
<li><a href="#prevent-passing-through-static-part-of-world">Prevent passing through static part of world</a></li>
<li><a href="#rope-spring-constraint">Rope Spring constraint</a></li>
</ul>
</li>
</ul>
<h2 id="operator">Operator</h2>
<h3 id="lifespan-decay">Lifespan decay</h3>

<table>
<thead>
<tr>
<th>Lifespan decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_decay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>35435</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>This enables particles to be destroyed by the effect.</p><p>All effects should have a Decay Operator (usually Lifespan Decay) unless you’re certain that the particles will get destroyed by some other means (usually code.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="radius-scale">Radius scale</h3>

<table>
<thead>
<tr>
<th>Radius scale</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_interpolateradius</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>32380</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Scales particles from the start to end scale over the specified time. Multiple Radius Scale operators can be used in an effect as long as their time coverage doesn’t overlap.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-basic">Movement basic</h3>

<table>
<thead>
<tr>
<th>Movement basic</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_basicmovement</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29027</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Enables basic movement for particles. (“Basic” in the sense of <i>fundamental</i> rather than simplistic.)</p><p>It’s not a bad idea to always add Movement Basic to new effects; if it ends up being spatially static later, you can remove the Operator for a tiny performance gain.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>gravity</td>
<td></td>
<td>Gravitational effect on the particles.</td>
</tr>
</tbody>
</table><h3 id="alpha-fade-out-simple">Alpha fade out simple</h3>

<table>
<thead>
<tr>
<th>Alpha fade out simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_fadeoutsimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23380</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles out over time.</p><p><b>proportional fade out time</b> is a percentage of the particle’s lifetime, expressed as a range between 0 and 1. (So a setting of 0.25 on a particle with a 4-second lifetime would start fading out 3 seconds after being emitted, and would take 1 second to fade out completely.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="alpha-fade-in-simple">Alpha fade in simple</h3>

<table>
<thead>
<tr>
<th>Alpha fade in simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_fadeinsimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18427</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles in over time.</p><p><b>proportional fade in time</b> is a percentage of the particle’s lifetime, expressed as a range between 0 and 1. (So a setting of 0.5 on a particle with a 4-second lifetime would take 2 seconds to fade in completely.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="color-fade">Color fade</h3>

<table>
<thead>
<tr>
<th>Color fade</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_colorinterpolate</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>15575</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Within the specified time, each particle fades from its color at <b>fade_start_time</b> to <b>color_fade</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-lock-to-control-point">Movement lock to control point</h3>

<table>
<thead>
<tr>
<th>Movement lock to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_positionlock</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>15184</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Causes particles to inherit the movement (and optionally rotation) of a control point.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="ramp-scalar-linear-simple">Ramp scalar linear simple</h3>

<table>
<thead>
<tr>
<th>Ramp scalar linear simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rampscalarlinearsimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>9981</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-basic">Rotation basic</h3>

<table>
<thead>
<tr>
<th>Rotation basic</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_spinupdate</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>7096</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>This simply enables rotation through the effect’s Base Properties (<b>rotation_speed</b>) or through the initializer “Rotation Speed Random”.</p><p>Particle rotation can also be achieved with the operators “Rotation Spin Roll” and “Rotation Spin Yaw”, which do not require the “Rotation Basic” operator.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="noise-vector">Noise vector</h3>

<table>
<thead>
<tr>
<th>Noise vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_vectornoise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5003</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps a noise function to any exposed vector. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets.</p><p>This creates a range of results that are non-random but vary based on creation time and position.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="oscillate-vector">Oscillate vector</h3>

<table>
<thead>
<tr>
<th>Oscillate vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_oscillatevector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3375</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="ramp-scalar-linear-random">Ramp scalar linear random</h3>

<table>
<thead>
<tr>
<th>Ramp scalar linear random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rampscalarlinear</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3117</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifespan-endcap-timed-decay">Lifespan endcap timed decay</h3>

<table>
<thead>
<tr>
<th>Lifespan endcap timed decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_endcaptimeddecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2893</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lerp-endcap-scalar">Lerp endcap scalar</h3>

<table>
<thead>
<tr>
<th>Lerp endcap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_lerpendcapscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2506</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="alpha-fade-and-decay">Alpha fade and decay</h3>

<table>
<thead>
<tr>
<th>Alpha fade and decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_fadeandkill</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2355</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Essentially combines the three operators “Lifespan Decay”, “Alpha Fade In Simple”, and “Alpha Fade Out Simple”.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-lock-to-bone">Movement lock to bone</h3>

<table>
<thead>
<tr>
<th>Movement lock to bone</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_locktobone</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2344</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="oscillate-scalar">Oscillate scalar</h3>

<table>
<thead>
<tr>
<th>Oscillate scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_oscillatescalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2253</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="alpha-fade-out-random">Alpha fade out random</h3>

<table>
<thead>
<tr>
<th>Alpha fade out random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_fadeout</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2231</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles out over a random period of time within the specified range.</p><p>Unlike “Alpha Fade Out Simple”, this operator has an option to define your range in seconds rather than a percentage of the particle’s lifespan. To use seconds, simply turn the <b>proportional</b> property off.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-distance-to-control-point-to-scalar">Remap distance to control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance to control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_distancetocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1566</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-skin-to-bones-rigid">Movement skin to bones rigid</h3>

<table>
<thead>
<tr>
<th>Movement skin to bones rigid</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_snapshotrigidskintobones</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1536</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="inherit-attribute-from-parent-particle">Inherit attribute from parent particle</h3>

<table>
<thead>
<tr>
<th>Inherit attribute from parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_inheritfromparentparticles</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1385</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Assigns a parent particle’s attribute to each particle within the system.</p><p>This differs from the initializer “Inherit Initial Value from Parent Particle” in that the parent’s attribute will be inherited every frame in real-time.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="noise-scalar">Noise scalar</h3>

<table>
<thead>
<tr>
<th>Noise scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_noise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1337</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps a noise function to any exposed scalar. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets.</p><p>This creates a range of results that are non-random but vary based on creation time and position.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-spin-roll">Rotation spin roll</h3>

<table>
<thead>
<tr>
<th>Rotation spin roll</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_spin</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1283</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Rotates each particle along the “roll” axis.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-rotate-particle-around-axis">Movement rotate particle around axis</h3>

<table>
<thead>
<tr>
<th>Movement rotate particle around axis</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_movementrotateparticlearoundaxis</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1230</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="alpha-fade-in-random">Alpha fade in random</h3>

<table>
<thead>
<tr>
<th>Alpha fade in random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_fadein</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1064</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles in over a random period of time within the specified range.</p><p>Unlike “Alpha Fade In Simple”, this operator has an option to define your range in seconds rather than a percentage of the particle’s lifespan. To use seconds, simply turn the <b>proportional</b> property off.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifespan-minimum-alpha-decay">Lifespan minimum alpha decay</h3>

<table>
<thead>
<tr>
<th>Lifespan minimum alpha decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_alphadecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1047</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-orient-relative-to-cp">Rotation orient relative to CP</h3>

<table>
<thead>
<tr>
<th>Rotation orient relative to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_orient2dreltocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>985</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="ramp-scalar-spline-random">Ramp scalar spline random</h3>

<table>
<thead>
<tr>
<th>Ramp scalar spline random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rampscalarspline</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>978</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-dampen-relative-to-control-point">Movement dampen relative to control point</h3>

<table>
<thead>
<tr>
<th>Movement dampen relative to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_dampentocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>896</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Drains a particle’s internal velocity as it approaches the specified control point. If no other forces are acting on it, the particle will eventually stop.</p><p>This can be used with operator “Movement Lock to Control Point” (and its distance fade property) to have a control point “capture” particles near it then draw them along. It can also lock endpoints of a line of particles while allowing the middle section to move freely.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-max-velocity">Movement max velocity</h3>

<table>
<thead>
<tr>
<th>Movement max velocity</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_maxvelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>871</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="clamp-scalar">Clamp scalar</h3>

<table>
<thead>
<tr>
<th>Clamp scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_clampscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>826</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Limits the specified scalar’s value to a range between <b>output minimum</b> and <b>output maximum</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-set-to-control-point">Movement set to control point</h3>

<table>
<thead>
<tr>
<th>Movement set to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_settocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>782</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="oscillate-scalar-simple">Oscillate scalar simple</h3>

<table>
<thead>
<tr>
<th>Oscillate scalar simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_oscillatescalarsimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>737</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-child-control-points-from-particle-positions">Set child control points from particle positions</h3>

<table>
<thead>
<tr>
<th>Set child control points from particle positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setchildcontrolpoints</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>685</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="cull-when-crossing-sphere">Cull when crossing sphere</h3>

<table>
<thead>
<tr>
<th>Cull when crossing sphere</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_distancecull</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>676</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Instantly destroys particles when they pass the specified spherical threshold.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-place-on-ground">Movement place on ground</h3>

<table>
<thead>
<tr>
<th>Movement place on ground</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_movementplaceonground</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>632</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>if ( m_nRefCP1 &gt; -1 ){	if ( ( pParticles-&gt;GetControlPointAtCurrentTime( m_nRefCP1 ) - pCtx-&gt;m_vecPrevPos1 ).Length() &gt; m_flTolerance )	{		bDirty = true;		pCtx-&gt;m_vecPrevPos1 = pParticles-&gt;GetControlPointAtCurrentTime( m_nRefCP1 );		pCtx-&gt;m_flLerpTime = pParticles-&gt;m_flCurTime;	}}</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-points-from-particle-positions">Set control points from particle positions</h3>

<table>
<thead>
<tr>
<th>Set control points from particle positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointstoparticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>590</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-per-child-control-point-from-particle-positions">Set per child control point from particle positions</h3>

<table>
<thead>
<tr>
<th>Set per child control point from particle positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setperchildcontrolpoint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>575</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lerp-initial-scalar">Lerp initial scalar</h3>

<table>
<thead>
<tr>
<th>Lerp initial scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_lerpscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>506</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-speed-to-scalar">Remap speed to scalar</h3>

<table>
<thead>
<tr>
<th>Remap speed to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapspeed</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>501</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-to-scalar">Remap control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcptoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>479</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-percentage-between-two-control-points-to-scalar">Remap percentage between two control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap percentage between two control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_percentagebetweencps</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>472</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifespan-minimum-radius-decay">Lifespan minimum radius decay</h3>

<table>
<thead>
<tr>
<th>Lifespan minimum radius decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_radiusdecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>427</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-maintain-positon-along-path">Movement maintain positon along path</h3>

<table>
<thead>
<tr>
<th>Movement maintain positon along path</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_maintainsequentialpath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>411</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-float">Set Float</h3>

<table>
<thead>
<tr>
<th>Set Float</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setfloat</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>397</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-skin-to-bones">Movement skin to bones</h3>

<table>
<thead>
<tr>
<th>Movement skin to bones</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_snapshotskintobones</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>377</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-direction-to-cp-to-vector">Remap direction to CP to vector</h3>

<table>
<thead>
<tr>
<th>Remap direction to CP to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapdirectiontocptovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>370</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-to-vector">Remap control point to vector</h3>

<table>
<thead>
<tr>
<th>Remap control point to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcptovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>328</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-lock-to-saved-position-along-path">Movement lock to saved position along path</h3>

<table>
<thead>
<tr>
<th>Movement lock to saved position along path</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_locktosavedsequentialpath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>283</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-velocity-to-vector">Remap velocity to vector</h3>

<table>
<thead>
<tr>
<th>Remap velocity to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapvelocitytovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>255</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="oscillate-vector-simple">Oscillate vector simple</h3>

<table>
<thead>
<tr>
<th>Oscillate vector simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_oscillatevectorsimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>239</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="ramp-scalar-spline-simple">Ramp scalar spline simple</h3>

<table>
<thead>
<tr>
<th>Ramp scalar spline simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rampscalarsplinesimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>229</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="inherit-attribute-from-parent-particle-1">Inherit attribute from parent particle</h3>

<table>
<thead>
<tr>
<th>Inherit attribute from parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_inheritfromparentparticlesv2</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>222</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotate-vector-random">Rotate vector random</h3>

<table>
<thead>
<tr>
<th>Rotate vector random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rotatevector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>220</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-lerp-to-hitbox">Movement lerp to hitbox</h3>

<table>
<thead>
<tr>
<th>Movement lerp to hitbox</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_movetohitbox</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>185</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-direction-to-vector">Remap control point direction to vector</h3>

<table>
<thead>
<tr>
<th>Remap control point direction to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcontrolpointdirectiontovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>172</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-orient-to-2d-direction">Rotation orient to 2d direction</h3>

<table>
<thead>
<tr>
<th>Rotation orient to 2d direction</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_orientto2ddirection</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>172</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="color-fade-random">Color fade random</h3>

<table>
<thead>
<tr>
<th>Color fade random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_colorinterpolaterandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>169</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-scalar">Remap scalar</h3>

<table>
<thead>
<tr>
<th>Remap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>162</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps any exposed scalar’s value to any other scalar on an ongoing basis.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="color-light-from-control-point">Color light from control point</h3>

<table>
<thead>
<tr>
<th>Color light from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_controlpointlight</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>161</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-cp-offset-to-cp-percentage-between-two-control-points">Set CP offset to CP percentage between two control points</h3>

<table>
<thead>
<tr>
<th>Set CP offset to CP percentage between two control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_cpoffsettopercentagebetweencps</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>153</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-from-cp-forward-orientation">Rotation from CP forward orientation</h3>

<table>
<thead>
<tr>
<th>Rotation from CP forward orientation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcporientationtoyaw</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>137</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-cp-orientaton-to-rotations">Remap CP orientaton to rotations</h3>

<table>
<thead>
<tr>
<th>Remap CP orientaton to rotations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcporientationtorotations</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>116</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Two New Options: <br><b>Use Quoternions Internally :</b><br> will use the Control points Matrix to extract Quoternion Rotations and apply that to the Orientation of the Particle. <br><br><b>Write Normal instead of Rotation :</b><br> is a sub section of Use Quaternion and will extract the CP Quoternion Fwd (X) Direction and map it to the Particle Normal. <br><br>While Off operator will work as before.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lerp-endcap-vector">Lerp endcap vector</h3>

<table>
<thead>
<tr>
<th>Lerp endcap vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_lerpendcapvector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>109</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="normalize-vector">Normalize vector</h3>

<table>
<thead>
<tr>
<th>Normalize vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_normalizevector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>98</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-distance-between-two-control-points-to-scalar">Remap distance between two control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance between two control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_distancebetweencps</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>96</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-distance-between-two-control-points-to-scalar-1">Remap distance between two control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance between two control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_distancebetweencpstocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>90</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-game-visibility-scalar">Remap game visibility scalar</h3>

<table>
<thead>
<tr>
<th>Remap game visibility scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapvisibilityscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>88</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-loop-inside-sphere">Movement loop inside sphere</h3>

<table>
<thead>
<tr>
<th>Movement loop inside sphere</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_movementloopinsidesphere</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>80</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-particle-count-on-endcap-scalar">Remap particle count on endcap scalar</h3>

<table>
<thead>
<tr>
<th>Remap particle count on endcap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapparticlecountonscalarendcap</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>78</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="clamp-vector">Clamp vector</h3>

<table>
<thead>
<tr>
<th>Clamp vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_clampvector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>74</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Limits the specified vector’s value to a range between <b>output minimum</b> and <b>output maximum</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-match-particle-velocities">Movement match particle velocities</h3>

<table>
<thead>
<tr>
<th>Movement match particle velocities</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_velocitymatchingforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>68</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Forces particles to inherit the velocity of the first one emitted. Can copy the recorded value to a control point.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="restart-effect-after-duration">Restart effect after duration</h3>

<table>
<thead>
<tr>
<th>Restart effect after duration</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_restartafterduration</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>64</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-game-visibility-of-cp-to-scalar">Remap game visibility of CP to scalar</h3>

<table>
<thead>
<tr>
<th>Remap game visibility of CP to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcpvisibilitytoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>64</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-difference-of-sequential-particle-vector-to-scalar">Remap difference of sequential particle vector to Scalar</h3>

<table>
<thead>
<tr>
<th>Remap difference of sequential particle vector to Scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_differencepreviousparticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>58</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-particle-count-to-scalar">Remap particle count to scalar</h3>

<table>
<thead>
<tr>
<th>Remap particle count to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapparticlecounttoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>51</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-maintain-offset">Movement maintain offset</h3>

<table>
<thead>
<tr>
<th>Movement maintain offset</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_movementmaintainoffset</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>51</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-cp-orientation-to-cp-direction">Set CP orientation to CP direction</h3>

<table>
<thead>
<tr>
<th>Set CP orientation to CP direction</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcporientationtodirection</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>47</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="cull-when-crossing-plane">Cull when crossing plane</h3>

<table>
<thead>
<tr>
<th>Cull when crossing plane</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_planecull</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>46</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Instantly destroys particles when they pass the specified plane.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-percentage-between-two-control-points-to-vector">Remap percentage between two control points to vector</h3>

<table>
<thead>
<tr>
<th>Remap percentage between two control points to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_percentagebetweencpsvector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>35</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-scalar-once-timed">Remap scalar once timed</h3>

<table>
<thead>
<tr>
<th>Remap scalar once timed</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapscalaroncetimed</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>33</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="cycle-scalar">Cycle Scalar</h3>

<table>
<thead>
<tr>
<th>Cycle Scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_cyclescalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>33</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifespan-from-endcap-decay">Lifespan from endcap decay</h3>

<table>
<thead>
<tr>
<th>Lifespan from endcap decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_endcapdecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>31</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-vector-to-cp">Remap vector to CP</h3>

<table>
<thead>
<tr>
<th>Remap vector to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapvectortocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-vec">Set Vec</h3>

<table>
<thead>
<tr>
<th>Set Vec</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setvec</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>27</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lerp-initial-vector">Lerp initial vector</h3>

<table>
<thead>
<tr>
<th>Lerp initial vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_lerpvector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>27</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-cp-orientation-to-ground-normal">Set CP orientation to ground normal</h3>

<table>
<thead>
<tr>
<th>Set CP orientation to ground normal</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcporientationtogroundnormal</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>21</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="pin-particle-to-control-point">Pin Particle to control point</h3>

<table>
<thead>
<tr>
<th>Pin Particle to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_pinparticletocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>20</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-dot-product-to-scalar">Remap dot product to scalar</h3>

<table>
<thead>
<tr>
<th>Remap dot product to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapdotproducttoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>19</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-lock-to-saved-position-along-path-1">Movement lock to saved position along path</h3>

<table>
<thead>
<tr>
<th>Movement lock to saved position along path</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_locktosavedsequentialpathv2</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>19</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifespan-maintain-count-decay">Lifespan maintain count decay</h3>

<table>
<thead>
<tr>
<th>Lifespan maintain count decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_decaymaintaincount</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="reinitalize-on-endcap-scalar-random">Reinitalize on endcap scalar random</h3>

<table>
<thead>
<tr>
<th>Reinitalize on endcap scalar random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_reinitializescalarendcap</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>17</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-cp-velocity-to-vector">Remap CP velocity to vector</h3>

<table>
<thead>
<tr>
<th>Remap CP velocity to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcpvelocitytovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>7</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-vector-from-control-point">Set vector from control point</h3>

<table>
<thead>
<tr>
<th>Set vector from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcptovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="movement-lerp-to-initial-position-relative-to-cp">Movement Lerp to Initial Position relative to CP</h3>

<table>
<thead>
<tr>
<th>Movement Lerp to Initial Position relative to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_lerptoinitialposition</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This operator moves particles back to their starting point relative to a control point.  It interpolates them, so the strength of the move (and inversely, how much other forces can move them) can be modulated by lifespan/curve/random range/whatever.  For example they can fly off into space, then reassemble themselves over time into their original pattern.  The original position can be anything – a position within sphere, grid, ring, snapshot, etc.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
<th>Tooltip</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.The interpolation factor will determine how fast/strong the effect is.<b>This field is the control point that is specified for the relative position.</b></td>
<td>Initial Position Reference CP</td>
</tr>
<tr>
<td>interpolation amount</td>
<td>float</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.<b>The interpolation factor will determine how fast/strong the effect is.  This can be mapped to a curve or control point to modify this value.</b></td>
<td>How strong is this interpolation to the initial position?</td>
</tr>
</tbody>
</table><h3 id="calculate-vector-attribute">Calculate vector attribute</h3>

<table>
<thead>
<tr>
<th>Calculate vector attribute</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_calculatevectorattribute</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This lets you specify up to 2 vector attributes (with weights), and up to two control points (with offsets and weights), plus an initial value and a final scale (both vectors). It then does this calculation:<blockquote>Output_attribute = final scale * ( start value + inputscale1<em>inputfield1 + inputscale2</em>inputfield2 + controlpoint1*controlpointscale1 + controlpoint2 * controlpoint2scale);</blockquote>     (Then, If the output attribute is “particle normal”, it will normalize it).<br><br>This has many uses, and can mix attributes together, normalize attributes, scale them, offset them, etc.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-on-endcap-scalar">Remap on endcap scalar</h3>

<table>
<thead>
<tr>
<th>Remap on endcap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapscalarendcap</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-distance-to-line-between-2-control-points-to-vector">Remap distance to line between 2 control points to vector</h3>

<table>
<thead>
<tr>
<th>Remap distance to line between 2 control points to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapdistancetolinesegmenttovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-orientaton-to-rotation">Remap control point orientaton to rotation</h3>

<table>
<thead>
<tr>
<th>Remap control point orientaton to rotation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcontrolpointorientationtorotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>4</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This operator is intended for sprite based renderers.  It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
<th>Tooltip</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. This field is for the rotation you wish to set on the sprites.</td>
<td>Rotation value to change on particle</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. This field is for the referenced control point.</td>
<td>Control Point to reference for rotation</td>
</tr>
<tr>
<td>offset of rotation</td>
<td>float</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. <b>This field allows an offset to be set, so if the CP is at 90 degrees, but you want the sprite to be 180, you can put 90 here.</b></td>
<td>How much to offset particles rotation for CP’s rotation in degrees</td>
</tr>
<tr>
<td>control point axis</td>
<td>integer</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. <b>This is the control point axis you wish to drive the sprite rotation. You can check the particle preview panel and the X/Y/Z value specified there is the same here. So if you set the Z component, then the value shown in the particle preview for rotation on Z should be what is set on the sprite’s rotation.</b></td>
<td>The axis to use for particle rotation - use particle preview to test.</td>
</tr>
</tbody>
</table><h3 id="remap-distance-to-line-between-2-control-points-to-scalar">Remap distance to line between 2 control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance to line between 2 control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapdistancetolinesegmenttoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-percentage-between-two-cps-to-lerp-cps-to-scalar">Remap percentage between two cps to lerp CPs to scalar</h3>

<table>
<thead>
<tr>
<th>Remap percentage between two cps to lerp CPs to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_percentagebetweencplerpcps</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-to-velocity">Remap control point to velocity</h3>

<table>
<thead>
<tr>
<th>Remap control point to velocity</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcptovelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="point-vector-at-next-particle-position">Point vector at next particle position</h3>

<table>
<thead>
<tr>
<th>Point vector at next particle position</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_pointvectoratnextparticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="init">Init</h2>
<h3 id="lifetime-random">Lifetime random</h3>

<table>
<thead>
<tr>
<th>Lifetime random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomlifetime</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>33523</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Defines the lifetime of each particle in seconds, chosen randomly, between <b>lifetime_min</b> and <b>lifetime_max</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="radius-random">Radius Random</h3>

<table>
<thead>
<tr>
<th>Radius Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomradius</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29028</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes each particle with a random radius within the specified range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-random">Rotation random</h3>

<table>
<thead>
<tr>
<th>Rotation random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomrotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>24297</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Randomly picks an initial rotation value for each particle within the specified range. The axis is chosen through the <b>rotation field</b> property.</p><p><b><i>NOTE</i></b>: The properties <b>yaw_offset_min</b> and <b>yaw_offset_max</b> are mis-named at the time of this writing. They should instead read “rotation min” and “rotation max” - these define the range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="color-random">Color Random</h3>

<table>
<thead>
<tr>
<th>Color Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomcolor</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23577</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes each particle with a random color within the specified range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-within-sphere-random">Position within sphere random</h3>

<table>
<thead>
<tr>
<th>Position within sphere random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createwithinsphere</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>22661</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Randomly spawns a particle within a sphere that’s centered on the specified control point.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>radius min</td>
<td>float</td>
<td>Minimum distance to spawn from the center of the sphere.</td>
</tr>
<tr>
<td>radius max</td>
<td>float</td>
<td>Maximum distance to spawn from the center of the sphere.</td>
</tr>
<tr>
<td>distance bias</td>
<td>vector</td>
<td>A bias to the distribution of particles in the system in X Y Z relative to each axis. 1 1 0 will create particles only in the X Y plane, while 1 1 10 will create roughly 10 times as many particles near the top and bottom of the sphere as on the X Y parts. Useful for creating discs, rings, and polar effects.</td>
</tr>
<tr>
<td>distance bias abs</td>
<td>vector</td>
<td>Setting any axis to one will eliminate particles from one hemisphere of the distribution. Can be used to create hemispheres, quarter spheres, etc. Use wil distance bias to alter the effect. Use negative values in distance bias to flip the hemisphere from one side to the other.</td>
</tr>
<tr>
<td>speed min</td>
<td>float</td>
<td>Minimum initial speed of the particle emitted outward from the sphere.</td>
</tr>
<tr>
<td>speed max</td>
<td>float</td>
<td>Maximum initial speed of the particle emitted outward from the sphere.</td>
</tr>
<tr>
<td>speed rand exp</td>
<td>float</td>
<td>The exponent which determines the biasing of particles towards one end or the other of the random range.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Local space minimum initial speed of the particle in x y z.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Local space maximum initial speed of the particle in x y z.</td>
</tr>
</tbody>
</table><h3 id="alpha-random">Alpha Random</h3>

<table>
<thead>
<tr>
<th>Alpha Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomalpha</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18841</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Particles will be created with a random alpha value within the specified range (0-255).</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-modify-offset-random">Position modify offset random</h3>

<table>
<thead>
<tr>
<th>Position modify offset random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_positionoffset</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>16846</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Moves the initial position of a particle in world or local space relative to its emission point.<p>Generally used in combination with other Position initializers. For example, it can be used to emit particles along a line while still using parts of a sphere emitter.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>local coords</td>
<td>boolean</td>
<td>This bool (0/1) sets where to use world or local (emitter) space to do the offset.</td>
</tr>
<tr>
<td>proportional</td>
<td>boolean</td>
<td>This bool (0/1) sets whether to treat the offset values as an amount relative to the particle’s radius. For example, if the offset is set to 0 0 1, and two particles have a radii of 32 and 64, they’d be moved vertically 32 and 64 units respectively.</td>
</tr>
</tbody>
</table><h3 id="sequence-random">Sequence Random</h3>

<table>
<thead>
<tr>
<th>Sequence Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomsequence</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>12637</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>When using a multi-frame texture, this allows particles to randomly start at a minimum and maximum supplied frame.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-noise">Velocity noise</h3>

<table>
<thead>
<tr>
<th>Velocity noise</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initialvelocitynoise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>10100</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Allows particle velocity to be initialized to a select range via a noise function. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets. This creates a range of results that are non-random but vary based on creation time and position.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-yaw-flip-random">Rotation yaw flip random</h3>

<table>
<thead>
<tr>
<th>Rotation yaw flip random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomyawflip</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>8320</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-particle-count-to-scalar-1">Remap particle count to scalar</h3>

<table>
<thead>
<tr>
<th>Remap particle count to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapparticlecounttoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6822</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-speed-random">Rotation speed random</h3>

<table>
<thead>
<tr>
<th>Rotation speed random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomrotationspeed</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5335</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-along-ring">Position along ring</h3>

<table>
<thead>
<tr>
<th>Position along ring</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_ringwave</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5137</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions along a whole or partial ring.</p><p>Like “Position Within Sphere Random”, this initializer has additional functionality that can impart radial force to particles via <b>min initial speed</b> and <b>max initial speed</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>particles per orbit</td>
<td>float</td>
<td>This along with turning on “even distribution” will evenly space the particles around the ring using X particles</td>
</tr>
<tr>
<td>even distribution</td>
<td>boolean</td>
<td>Enabling even distribution will evenly space the particles around the ring.</td>
</tr>
</tbody>
</table><h3 id="remap-scalar-1">Remap scalar</h3>

<table>
<thead>
<tr>
<th>Remap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3301</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps any exposed scalar’s initial value to any other scalar.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="trail-length-random">Trail length random</h3>

<table>
<thead>
<tr>
<th>Trail length random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomtraillength</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3183</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-to-scalar-1">Remap control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapcptoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2740</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-from-parent-particles">Position from parent particles</h3>

<table>
<thead>
<tr>
<th>Position from parent particles</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createfromparentparticles</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2499</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-modify-place-on-ground">Position modify place on ground</h3>

<table>
<thead>
<tr>
<th>Position modify place on ground</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_positionplaceonground</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2262</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>“Snaps” each particle to the ground (or a specified offset above the ground.)</p><p>Note that this operator only searches for ground BELOW its current position - if the particle is already below the ground, it won’t snap to the ground above. If there’s any doubt, simply add a Position Modify Offset Random initializer above this one in the initializer stack.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-skin-to-bones-from-cp-snapshot">Position skin to bones from CP snapshot</h3>

<table>
<thead>
<tr>
<th>Position skin to bones from CP snapshot</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initskinnedpositionfromcpsnapshot</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1983</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-yaw-random">Rotation yaw random</h3>

<table>
<thead>
<tr>
<th>Rotation yaw random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomyaw</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1955</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-noise-to-scalar">Remap noise to scalar</h3>

<table>
<thead>
<tr>
<th>Remap noise to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_creationnoise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1937</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Allows any scalar parameter to be initialized to a select range via a noise function. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets. This creates a range of results that are non-random but vary based on creation time and position.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>noise scale</td>
<td>float</td>
<td>This sets the scale of the time part of the noise function - based on particle spawn time. Larger numbers will appear increasingly random, while very small numbers will map to a similar area of the noise and look very similar.</td>
</tr>
<tr>
<td>noise scale loc</td>
<td>float</td>
<td>This sets the scale of the spatial part of the noise function - based on particle spawn location. Larger numbers will appear increasingly random, while very small numbers will map to a similar area of the noise and look very similar. Time noise is added to spatial noise, so set one or the other to zero in order to receive no effect from that portion of the function.</td>
</tr>
<tr>
<td>offset loc</td>
<td>vector</td>
<td>This sets the offset on the noise function to draw from. Two initial scalar noise functions set to different outputs (say alpha and radius) set to the same coordinate scales will behave the same. Offsets allow for the same scale mapping, but at a different part of the noise. So for example all small radius particles may have a high alpha rather than a low one if the offset is used.</td>
</tr>
<tr>
<td>abs val</td>
<td>boolean</td>
<td>Noise returns -1 to 1 which is mapped to the output range. Using absolute value bool (0/1) , the output can have sudden shifts in direction as the number approaches zero and then bounces back into positives instead of going into negatives.</td>
</tr>
<tr>
<td>abs val inv</td>
<td>boolean</td>
<td>Essentially flips the curve created by using the absolute value flag. So instead of getting sharp valleys, you get sharp peaks. The math is 1 minus the absolute value of the noise.</td>
</tr>
<tr>
<td>offset</td>
<td>float</td>
<td>This sets the offset on the noise function to draw from. Two initial scalar noise functions set to different outputs (say alpha and radius) set to the same coordinate scales will behave the same. Offsets allow for the same scale mapping, but at a different part of the noise. So for example all small radius particles may have a high alpha rather than a low one if the offset is used.</td>
</tr>
</tbody>
</table><h3 id="inherit-attribute-from-parent-particle-2">Inherit attribute from parent particle</h3>

<table>
<thead>
<tr>
<th>Inherit attribute from parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_inheritfromparentparticles</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1738</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Assigns a parent particle’s attribute to each particle’s initial value for that attribute.</p><p>This differs from the operator “Inherit Attribute from Parent Particle” in that it runs only once, on particle initialization.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-modify-warp-random">Position modify warp random</h3>

<table>
<thead>
<tr>
<th>Position modify warp random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_positionwarp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1671</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Warps the initial position of a particle in world or local space relative to its emission point. Can be used to stretch initial emission shapes. A sphere can be stretched into an ovoid, or smashed.</p><p>Useful in addition to sphere emissions distance bias and absolute value to create squashed domes, rings (the elongated ring seen in Portal), etc. Warped particles’ initial speed is also warped by the corresponding amount. So particles that are stretched will have a higher initial velocity, while those that are squashed will have lower.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>warp time</td>
<td>float</td>
<td>Treats the min/max as start and end sizes for a warp that takes place over the specified time. So the emission placement of each new particle will be warped over time.</td>
</tr>
<tr>
<td>invert warp</td>
<td>boolean</td>
<td>In the case of a warp transition, it will make it run backwards (max to min).</td>
</tr>
</tbody>
</table><h3 id="velocity-random">Velocity random</h3>

<table>
<thead>
<tr>
<th>Velocity random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_velocityrandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1504</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-along-path-sequential">Position along path sequential</h3>

<table>
<thead>
<tr>
<th>Position along path sequential</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createsequentialpath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1480</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions sequentially along a line between two control points.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-control-point-to-vector-1">Remap control point to vector</h3>

<table>
<thead>
<tr>
<th>Remap control point to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapcptovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1354</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="scalar-random">Scalar random</h3>

<table>
<thead>
<tr>
<th>Scalar random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1144</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows any exposed scalar (such as radius, alpha, lifetime, etc.) to be initialized with a random value within the specified range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-from-cp-snapshot">Init from CP snapshot</h3>

<table>
<thead>
<tr>
<th>Init from CP snapshot</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initfromcpsnapshot</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1082</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="normal-align-to-cp">Normal align to CP</h3>

<table>
<thead>
<tr>
<th>Normal align to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_normalaligntocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1057</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="sequence-two-random">Sequence two random</h3>

<table>
<thead>
<tr>
<th>Sequence two random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomsecondsequence</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>690</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-inherit-from-control-point">Velocity inherit from control point</h3>

<table>
<thead>
<tr>
<th>Velocity inherit from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_inheritvelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>676</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="offset-vector-to-vector">Offset vector to vector</h3>

<table>
<thead>
<tr>
<th>Offset vector to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_offsetvectortovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>658</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-initial-distance-to-control-point-to-scalar">Remap initial distance to control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap initial distance to control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_distancetocpinit</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>655</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-along-epitrochoid">Position along epitrochoid</h3>

<table>
<thead>
<tr>
<th>Position along epitrochoid</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createinepitrochoid</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>571</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions within an <a href="https://en.wikipedia.org/wiki/Epitrochoid">epitrochoid</a>.</p><p>Notably, this position initializer can be used to modify another position initializer if <b>offset from existing position</b> is checked. With the right combination of position initializers and epitrochoid settings, you can achieve positional noise with more coherence than simple random ranges offer.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-from-killed-parent-particle">Init from killed parent particle</h3>

<table>
<thead>
<tr>
<th>Init from killed parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initfromparentkilled</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>561</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="normal-lock-to-control-point">Normal lock to control point</h3>

<table>
<thead>
<tr>
<th>Normal lock to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_normallock</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>505</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-cp-orientation-to-rotation">Remap CP orientation to rotation</h3>

<table>
<thead>
<tr>
<th>Remap CP orientation to rotation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapinitialcpdirectiontorotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>413</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This operator is intended for sprite based renderers.  It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-within-box-random">Position within box random</h3>

<table>
<thead>
<tr>
<th>Position within box random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createwithinbox</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>382</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Randomly spawns a particle within the specified volume.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="normal-modify-offset-random">Normal modify offset random</h3>

<table>
<thead>
<tr>
<th>Normal modify offset random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_normaloffset</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>361</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifetime-from-sequence">Lifetime from sequence</h3>

<table>
<thead>
<tr>
<th>Lifetime from sequence</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_sequencelifetime</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>338</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Sets a particle’s lifespan based on the animation length of the sequence based at the given framerate. Used when a single particle type consists of many sequences with varying sequence lengths (some have 10 frames, others 60, but all must act appropriately without slow framerate, etc.)</p><p><i>Note:</i> If the ‘use animation rate as FPS’ flag of Render_Animated_Sprites has the same FPS settings, a particle will map it lifespan and animation together perfectly.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>framerate</td>
<td>float</td>
<td>Sets the desired FPS for the animation. This is mapped to lifespan according to the number of frames in the sequence the particle receives via a <b>sequence_random</b> or other sequence-defining initializer.</td>
</tr>
</tbody>
</table><h3 id="remap-initial-direction-to-cp-to-vector">Remap initial direction to CP to vector</h3>

<table>
<thead>
<tr>
<th>Remap initial direction to CP to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapinitialdirectiontocptovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>333</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-float">Init Float</h3>

<table>
<thead>
<tr>
<th>Init Float</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initfloat</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>323</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-set-from-control-point">Velocity set from control point</h3>

<table>
<thead>
<tr>
<th>Velocity set from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_velocityfromcp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>298</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-spin-yaw">Rotation spin yaw</h3>

<table>
<thead>
<tr>
<th>Rotation spin yaw</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_spinyaw</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>292</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Rotates each particle along the “yaw” axis.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="vector-component-random">Vector component random</h3>

<table>
<thead>
<tr>
<th>Vector component random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomvectorcomponent</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>243</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rotation-orient-relative-to-cp-1">Rotation orient relative to CP</h3>

<table>
<thead>
<tr>
<th>Rotation orient relative to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_orient2dreltocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>243</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-status-effect">Init Status Effect</h3>

<table>
<thead>
<tr>
<th>Init Status Effect</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_statuseffect</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>193</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-scalar-to-vector">Remap scalar to vector</h3>

<table>
<thead>
<tr>
<th>Remap scalar to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapscalartovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>193</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Upon particle initialization, remap any starting scalar (alpha, radius, etc.) to any starting vector (position, color, etc.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="vector-random">Vector random</h3>

<table>
<thead>
<tr>
<th>Vector random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomvector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>183</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-along-path-random">Position along path random</h3>

<table>
<thead>
<tr>
<th>Position along path random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createalongpath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>168</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions randomly along a line between two control points.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-along-path-sequential-1">Position along path sequential</h3>

<table>
<thead>
<tr>
<th>Position along path sequential</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createsequentialpathv2</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>163</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions sequentially along a line between two or more control points.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-on-spiral-sphere">Position on spiral sphere</h3>

<table>
<thead>
<tr>
<th>Position on spiral sphere</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createspiralsphere</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>101</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-qangie-in-cp-to-rotations">Remap QAngIe in CP to rotations</h3>

<table>
<thead>
<tr>
<th>Remap QAngIe in CP to rotations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapqanglestorotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>91</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="radius-from-cp-object">Radius from CP object</h3>

<table>
<thead>
<tr>
<th>Radius from CP object</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_radiusfromcpobject</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>69</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="globally-scale-initial-attributes">Globally Scale Initial Attributes</h3>

<table>
<thead>
<tr>
<th>Globally Scale Initial Attributes</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_globalscale</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>60</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-hitbox-to-closest-hitbox">Set hitbox to closest hitbox</h3>

<table>
<thead>
<tr>
<th>Set hitbox to closest hitbox</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_sethitboxtoclosest</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>48</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="sequence-from-control-point">Sequence from control point</h3>

<table>
<thead>
<tr>
<th>Sequence from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_sequencefromcp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>45</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-from-parent-cache">Position from parent cache</h3>

<table>
<thead>
<tr>
<th>Position from parent cache</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createfromplanecache</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>45</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="cull-relative-to-ray-trace-environment">Cull relative to ray trace environment</h3>

<table>
<thead>
<tr>
<th>Cull relative to ray trace environment</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_rtenvcull</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>44</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-from-control-points">Position from control points</h3>

<table>
<thead>
<tr>
<th>Position from control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createfromcps</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>38</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-cp-orientation-to-rotations">Init CP orientation to rotations</h3>

<table>
<thead>
<tr>
<th>Init CP orientation to rotations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapcporientationtorotations</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>35</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-vec">Init Vec</h3>

<table>
<thead>
<tr>
<th>Init Vec</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initvec</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="add-vector-to-vector">Add vector to vector</h3>

<table>
<thead>
<tr>
<th>Add vector to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_addvectortovector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>24</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-radial-random">Velocity radial random</h3>

<table>
<thead>
<tr>
<th>Velocity radial random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_velocityradialrandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-speed-to-scalar-1">Remap speed to scalar</h3>

<table>
<thead>
<tr>
<th>Remap speed to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapspeedtoscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps either a control point’s speed (effect-level) or each particle’s speed (particle-level) to a scalar value.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="lifetime-from-time-to-impact">Lifetime from time to impact</h3>

<table>
<thead>
<tr>
<th>Lifetime from time to impact</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_lifespanfromvelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>22</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-repulse-from-world">Velocity repulse from world</h3>

<table>
<thead>
<tr>
<th>Velocity repulse from world</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initialrepulsionvelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>21</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="alpha-window-threshold-random">Alpha window threshold random</h3>

<table>
<thead>
<tr>
<th>Alpha window threshold random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_randomalphawindowthreshold</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-with-phyllotaxis-distribution">Position with phyllotaxis distribution</h3>

<table>
<thead>
<tr>
<th>Position with phyllotaxis distribution</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_createphyllotaxis</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-away-from-hitbox-random">Velocity away from hitbox random</h3>

<table>
<thead>
<tr>
<th>Velocity away from hitbox random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_initialvelocityfromhitbox</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>11</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="position-modify-offset-relative-to-control-point">Position modify offset relative to control point</h3>

<table>
<thead>
<tr>
<th>Position modify offset relative to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_positionoffsettocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>8</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="velocity-from-normal-random">Velocity from normal random</h3>

<table>
<thead>
<tr>
<th>Velocity from normal random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_velocityfromnormal</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-initial-game-visibility-to-scalar">Remap initial game visibility to scalar</h3>

<table>
<thead>
<tr>
<th>Remap initial game visibility to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_remapinitialvisibilityscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="color-lit-per-particle">Color lit per particle</h3>

<table>
<thead>
<tr>
<th>Color lit per particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_colorlitperparticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="init-vector-attribute-from-a-list-of-values">Init vector attribute from a list of values</h3>

<table>
<thead>
<tr>
<th>Init vector attribute from a list of values</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_pointlist</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="move-particles-between-2-control-points">Move particles between 2 control points</h3>

<table>
<thead>
<tr>
<th>Move particles between 2 control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_movebetweenpoints</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Moves the particles between 2 control points at a value between the minimum and maximum speed. Can be extremely useful for particle tracers, laser sights/beams, and Halo-esque sniper-rifle trails.</p><p><i>Note:</i> Normally, this initializer moves particles to the end control point and leaves them there (i.e., if new particles are created, they will spawn at the end control point and immediately vanish). To get around this, add a “Position Along Path Sequential” initializer with start and end control points of 0 ABOVE the “Move Particles Between 2 Control Points” entry.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>start offset</td>
<td>float</td>
<td>Offset of where the particles start relative to the starting control point and direction of movement.</td>
</tr>
<tr>
<td>end offset</td>
<td>float</td>
<td>The spread of the particles relative to the end control point. Think of this as how spray works with a gun.</td>
</tr>
</tbody>
</table><h3 id="position-modify-warp-from-scalar">Position modify warp from scalar</h3>

<table>
<thead>
<tr>
<th>Position modify warp from scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_positionwarpscalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="renderer">Renderer</h2>
<h3 id="render-sprites">Render sprites</h3>

<table>
<thead>
<tr>
<th>Render sprites</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rendersprites</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>26773</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Renders single- and multiple-frame sprites.</p><p>Multi-frame sequences can be animated or used to provide visual variation.</p><p>render_sprites is the workhorse renderer, and the one you’re likely to be using most of the time.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>depth bias</td>
<td>float</td>
<td>Offsets particle depth via the shader. This is more expensive than per particle offsets which can be achieved by using “visibility camera depth bias”</td>
</tr>
</tbody>
</table><h3 id="render-rope">Render rope</h3>

<table>
<thead>
<tr>
<th>Render rope</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_renderropes</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6160</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Ropes (which were named in a simpler time) are sequences of sprites streched across a set of points. Textures intended for use on rope particles are often tiled along one axis so they can be used to create long, thin, curved forms in 3D space.</p><p>Ropes can be difficult to work with, but are surprisingly powerful and versatile.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-sprite-trail">Render sprite trail</h3>

<table>
<thead>
<tr>
<th>Render sprite trail</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rendertrails</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3477</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Trails are sprites with additional built-in behavior that stretches them based on their speed over time.</p><p>Traditional use cases for trails include bullet tracers and sparks. Advanced users may also find them useful when particles need to be oriented in 3D space (a case that regular sprites handle poorly.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-deferred-light">Render deferred light</h3>

<table>
<thead>
<tr>
<th>Render deferred light</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_renderdeferredlight</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1943</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Renders one or more real-time (but not shadow-casting) light sources based on particle positions.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-projected">Render projected</h3>

<table>
<thead>
<tr>
<th>Render projected</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_renderprojected</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>591</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Renders projected textures, which are capable of certain behaviors that are otherwise difficult to achieve.</p><p>Take, for example, a large scorch-mark on the ground. If you used a flat sprite (even one oriented to the ground polygon on which it sat), it still wouldn’t look right if it crossed polygon boundaries that changed angles or elevation. A projected texture, however, will conform to the surfaces upon which it’s projected.</p><p><i>Note that unlike many other effect renderers, this one takes a VMAT rather than a VTEX. VMATs are authored in the Material Editor, and should be shader type “Projected Dota”.</i></p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-status-effect">Render Status Effect</h3>

<table>
<thead>
<tr>
<th>Render Status Effect</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_renderstatuseffect</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>199</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-screen-shake">Render screen shake</h3>

<table>
<thead>
<tr>
<th>Render screen shake</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_renderscreenshake</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>132</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-blobs">Render blobs</h3>

<table>
<thead>
<tr>
<th>Render blobs</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_renderblobs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>55</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-sound">Render sound</h3>

<table>
<thead>
<tr>
<th>Render sound</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rendersound</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>13</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-tree-shake">Render Tree Shake</h3>

<table>
<thead>
<tr>
<th>Render Tree Shake</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rendertreeshake</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="render-text">Render Text</h3>

<table>
<thead>
<tr>
<th>Render Text</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rendertext</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="emitter">Emitter</h2>
<h3 id="emit-continuously">Emit continuously</h3>

<table>
<thead>
<tr>
<th>Emit continuously</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_continuousemitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>20922</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Emits particles at the specified rate over time. By default, this emitter will continue to emit forever.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>start time</td>
<td>float</td>
<td>Time at which to begin emitting particles (seconds).</td>
</tr>
<tr>
<td>emit rate</td>
<td>float</td>
<td>Number of particles to spawn (per second).</td>
</tr>
<tr>
<td>emission duration</td>
<td>float</td>
<td>Length of time to continue emitting particles (seconds).</td>
</tr>
</tbody>
</table><h3 id="emit-instantaniously">Emit instantaniously</h3>

<table>
<thead>
<tr>
<th>Emit instantaniously</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_instantaneousemitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18907</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Emits the specified number of particles all at once and never repeats.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>particles to emit</td>
<td>integer</td>
<td>Number of particles to emit in a burst.</td>
</tr>
<tr>
<td>min particles to emit</td>
<td>integer</td>
<td><p>The minimum number of particles to emit in a burst. Any value other than -1 will tell the system to randomly emit a number of particles between this value and the num_to_emit value.</p></td>
</tr>
<tr>
<td>max emitted per frame</td>
<td>integer</td>
<td><p>The maximum number of particles to emit per frame.</p><p>For example, if the game is running at 30 frames per second and this value is set to 1, then 30 particles will be emitted in one second. Keep in mind that even though the particles are emitted at a different time, they will all die together at the same time. Therefore, if lifetime random is set to 2, then every particle regardless of when it was created will be removed after 2 seconds of the system’s lifetime.</p></td>
</tr>
</tbody>
</table><h3 id="emit-noise">Emit noise</h3>

<table>
<thead>
<tr>
<th>Emit noise</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_noiseemitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1385</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="emit-to-maintain-count">Emit to maintain count</h3>

<table>
<thead>
<tr>
<th>Emit to maintain count</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_maintainemitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>133</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Emits particles until it reaches the specified <b>count to maintain</b>, and then stops. Whenever particles are destroyed (by whatever means), the emitter will kick in again to bring the count back up to the max.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="force-gen">Force-Gen</h2>
<h3 id="pull-towards-control-point">Pull towards control point</h3>

<table>
<thead>
<tr>
<th>Pull towards control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_attracttocontrolpoint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3868</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Pulls particles toward the specified control point.</p><p>Can also be used to repel particles - simply use negative values for <b>amount of force</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="random-force">Random force</h3>

<table>
<thead>
<tr>
<th>Random force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_randomforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1092</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Generates a random force within the specified range that’s applied uniformly to all particles within the effect.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="twist-around-axis">Twist around axis</h3>

<table>
<thead>
<tr>
<th>Twist around axis</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_twistaroundaxis</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>860</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="curlnoise-force">CurlNoise force</h3>

<table>
<thead>
<tr>
<th>CurlNoise force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_curlnoiseforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>329</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset rate</td>
<td>vector</td>
<td>This will increment the noise offset each frame</td>
</tr>
<tr>
<td>noise scale</td>
<td>vector</td>
<td>Amplitude of the noise</td>
</tr>
<tr>
<td>curl</td>
<td>boolean</td>
<td>toggle between dnoise() and curlnoise()</td>
</tr>
</tbody>
</table><h3 id="turbulent-force">Turbulent force</h3>

<table>
<thead>
<tr>
<th>Turbulent force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_turbulenceforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>204</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="external-wind-force">External Wind force</h3>

<table>
<thead>
<tr>
<th>External Wind force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_externalwindforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>135</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="local-acceleraton-force">Local acceleraton force</h3>

<table>
<thead>
<tr>
<th>Local acceleraton force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_localaccelerationforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>105</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="time-varying-force">Time varying force</h3>

<table>
<thead>
<tr>
<th>Time varying force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_timevaryingforce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>55</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="force-based-on-distance-from-plane">Force based on distance from plane</h3>

<table>
<thead>
<tr>
<th>Force based on distance from plane</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_forcebasedondistancetoplane</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>19</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Applies a force to each particle based on its distance from a specified plane. (You can think of this as simply remapping a distance to a force range.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="create-vortices-from-parent-particles">Create vortices from parent particles</h3>

<table>
<thead>
<tr>
<th>Create vortices from parent particles</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_parentvortices</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>16</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="pre">Pre</h2>
<h3 id="set-single-control-point-position">Set single control point position</h3>

<table>
<thead>
<tr>
<th>Set single control point position</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setsinglecontrolpointposition</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2679</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows the manual positioning of a single control point.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-point-orientaton">Set control point orientaton</h3>

<table>
<thead>
<tr>
<th>Set control point orientaton</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointorientation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1240</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-point-positions">Set control point Positions</h3>

<table>
<thead>
<tr>
<th>Set control point Positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointpositions</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1039</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows the manual positioning of up to four control points.</p><p>If you’re only setting one CP, consider using “Set Single Control Point Position” instead.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-per-child-control-point-from-parent-control-points">Set per child control point from parent control points</h3>

<table>
<thead>
<tr>
<th>Set per child control point from parent control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setparentcontrolpointstochildcp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>716</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-cp-speed-to-cp">Remap CP speed to CP</h3>

<table>
<thead>
<tr>
<th>Remap CP speed to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapspeedtocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>656</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="hsv-shift-to-control-point">HSV Shift to control point</h3>

<table>
<thead>
<tr>
<th>HSV Shift to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_hsvshifttocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>584</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="stop-effect-after-duraton">Stop effect after duraton</h3>

<table>
<thead>
<tr>
<th>Stop effect after duraton</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_stopaftercpduration</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>520</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-point-from-cp-object-scale">Set control point from CP object scale</h3>

<table>
<thead>
<tr>
<th>Set control point from CP object scale</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointfromobjectscale</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>462</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-point-rotation">Set control point rotation</h3>

<table>
<thead>
<tr>
<th>Set control point rotation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointrotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>300</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-point-to-random-position">Set control point to random Position</h3>

<table>
<thead>
<tr>
<th>Set control point to random Position</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setrandomcontrolpointposition</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>131</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-cp-orientaton-to-point-at-second-cp">Set CP orientaton to point at second CP</h3>

<table>
<thead>
<tr>
<th>Set CP orientaton to point at second CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcporientationtopointatcp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>69</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-average-scalar-value-to-cp">Remap average scalar value to CP</h3>

<table>
<thead>
<tr>
<th>Remap average scalar value to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapaveragescalarvaluetocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>51</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="remap-cp-component-to-cp-component">Remap CP component to CP component</h3>

<table>
<thead>
<tr>
<th>Remap CP component to CP component</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_remapcptocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>47</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-control-point-to-impact-point">Set control point to impact point</h3>

<table>
<thead>
<tr>
<th>Set control point to impact point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointtoimpactpoint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>32</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="force-control-point-in-pet">Force Control Point In Pet</h3>

<table>
<thead>
<tr>
<th>Force Control Point In Pet</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_forcecontrolpointstub</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>31</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="enable-children-from-parent-particle-count">Enable children from parent particle count</h3>

<table>
<thead>
<tr>
<th>Enable children from parent particle count</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_enablechildrenfromparentparticlecount</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>27</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="repeatedly-trigger-child-group">Repeatedly Trigger Child Group</h3>

<table>
<thead>
<tr>
<th>Repeatedly Trigger Child Group</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_repeatedtriggerchildgroup</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>9</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>child group id</td>
<td>integer</td>
<td>Children with this Group ID specified will not fire when the system is created.Instead, they will fire based on the settings of this operator.  Group ID is available under the Base Properties as an Advanced Option of all particle systems.</td>
</tr>
<tr>
<td>cluster refire time min</td>
<td>float</td>
<td>This is the minimum time before random firings of a child.Children are selected randomly from any systems which match the Group ID and are not currently in-progress.  Once a child has finished, it will once again be available to fire.  To have multiple concurrent children of the same type, add multiple identicle children.Because the children are of an unknownable lifespan with each firing, sequential firing is not predictable, so it will always be random amongst available children.If more specific control is needed, multiple operators with multiple Group ID’s can be used.</td>
</tr>
<tr>
<td>cluster refire time max</td>
<td>float</td>
<td>This is the maximum time before random firings of a child.Children are selected randomly from any systems which match the Group ID and are not currently in-progress.  Once a child has finished, it will once again be available to fire.  To have multiple concurrent children of the same type, add multiple identicle children.Because the children are of an unknownable lifespan with each firing, sequential firing is not predictable, so it will always be random amongst available children.If more specific control is needed, multiple operators with multiple Group ID’s can be used.</td>
</tr>
<tr>
<td>cluster size min</td>
<td>integer</td>
<td>This is the minimum number of children to fire before triggering a cooldown period.The operator will pick a count each time it starts a cluster and fire that many children before cooling down for the specified period.</td>
</tr>
<tr>
<td>cluster size max</td>
<td>integer</td>
<td>This is the maximum number of children to fire before triggering a cooldown period.The operator will pick a count each time it starts a cluster and fire that many children before cooling down for the specified period.</td>
</tr>
<tr>
<td>cluster cooldown min</td>
<td>float</td>
<td>This is the minimum amount of time to cooldown after a cluster has fired.When the specified number of children have fired, the operator will cooldown for this long before triggering additional children.</td>
</tr>
<tr>
<td>cluster cooldown max</td>
<td>float</td>
<td>This is the maximum amount of time to cooldown after a cluster has fired.When the specified number of children have fired, the operator will cooldown for this long before triggering additional children.</td>
</tr>
<tr>
<td>cluster size</td>
<td>float</td>
<td>Number of children to fire before entering cooldown</td>
</tr>
<tr>
<td>cluster refire time</td>
<td>float</td>
<td>Time/RandRange/Etc. for firing off children</td>
</tr>
<tr>
<td>cluster cooldown</td>
<td>float</td>
<td>Cooldown between clusters of firings</td>
</tr>
</tbody>
</table><h3 id="set-control-point-component-to-scalar-expression">Set control point component to scalar expression</h3>

<table>
<thead>
<tr>
<th>Set control point component to scalar expression</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointfieldtoscalarexpression</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="ramp-control-point-linear-random">Ramp control point linear random</h3>

<table>
<thead>
<tr>
<th>Ramp control point linear random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_rampcplinearrandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>4</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="use-random-children-in-group">Use Random Children in Group</h3>

<table>
<thead>
<tr>
<th>Use Random Children in Group</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_chooserandomchildreningroup</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>4</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="set-dest-cp-field-1-if-source-cp-is-in-water">Set dest CP field 1 if source CP is in water</h3>

<table>
<thead>
<tr>
<th>Set dest CP field 1 if source CP is in water</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_setcontrolpointfieldtowater</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="constraint">Constraint</h2>
<h3 id="constrain-distance-to-control-point">Constrain distance to control point</h3>

<table>
<thead>
<tr>
<th>Constrain distance to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_constraindistance</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>446</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Locks particles’s positions to a specified radial range from a control point.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="collision-via-traces">Collision via traces</h3>

<table>
<thead>
<tr>
<th>Collision via traces</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_worldtraceconstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>318</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows particles to collide with scene geometry.</p><p><b>USE SPARINGLY!</b> Per-particle collision is one of the most expensive effects operations performance-wise. Also, make sure you always replace the <b>collision group</b> property “NONE” with “DEBRIS”.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>cp offset</td>
<td>vector</td>
<td>-----</td>
</tr>
<tr>
<td>collision mode</td>
<td>integer</td>
<td>Colission Modes :#define COLLISION_MODE_PER_PARTICLE_TRACE 0#define COLLISION_MODE_PER_FRAME_PLANESET 1#define COLLISION_MODE_INITIAL_TRACE_DOWN 2#define COLLISION_MODE_USE_NEAREST_TRACE 3</td>
</tr>
</tbody>
</table><h3 id="prevent-passing-through-a-plane">Prevent passing through a plane</h3>

<table>
<thead>
<tr>
<th>Prevent passing through a plane</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_planarconstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>312</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="constrain-distance-to-path-between-two-control-points">Constrain distance to path between two control points</h3>

<table>
<thead>
<tr>
<th>Constrain distance to path between two control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_constraindistancetopath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>306</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="constrain-particles-to-a-box">Constrain particles to a box</h3>

<table>
<thead>
<tr>
<th>Constrain particles to a box</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_boxconstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="prevent-passing-through-static-part-of-world">Prevent passing through static part of world</h3>

<table>
<thead>
<tr>
<th>Prevent passing through static part of world</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_worldcollideconstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="rope-spring-constraint">Rope Spring constraint</h3>

<table>
<thead>
<tr>
<th>Rope Spring constraint</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_ropespringconstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th></th>
</tr>
</thead>
<tbody></tbody>
</table>
