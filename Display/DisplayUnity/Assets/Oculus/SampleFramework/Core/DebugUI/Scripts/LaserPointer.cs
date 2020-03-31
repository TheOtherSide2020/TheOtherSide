/************************************************************************************

Copyright (c) Facebook Technologies, LLC and its affiliates. All rights reserved.  

See SampleFramework license.txt for license terms.  Unless required by applicable law 
or agreed to in writing, the sample code is provided “AS IS” WITHOUT WARRANTIES OR 
CONDITIONS OF ANY KIND, either express or implied.  See the license for specific 
language governing permissions and limitations under the license.

************************************************************************************/

using UnityEngine;
using System.Collections;
using UnityEngine.EventSystems;
using UnityEngine.UI;
using System;

public class LaserPointer : OVRCursor
{
    public enum LaserBeamBehavior
    {
        On,        // laser beam always on
        Off,        // laser beam always off
        OnWhenHitTarget,  // laser beam only activates when hit valid target
    }

    public GameObject cursorVisual;
    public Transform cameraRig;
    public float maxLength = 10.0f;

    private LaserBeamBehavior _laserBeamBehavior;

    public LaserBeamBehavior laserBeamBehavior
    {
        set {
            _laserBeamBehavior = value;
            if(laserBeamBehavior == LaserBeamBehavior.Off || laserBeamBehavior == LaserBeamBehavior.OnWhenHitTarget)
            {
                lineRenderer.enabled = false;
            }
            else
            {
                lineRenderer.enabled = true;
            }
        }
        get
        {
            return _laserBeamBehavior;
        }
    }
    private Vector3 _startPoint;
    private Vector3 _forward;
    private Vector3 _endPoint;
    private bool _hitTarget;
    private LineRenderer lineRenderer;
    private bool canMove;

    private void Awake()
    {
        lineRenderer = GetComponent<LineRenderer>();
    }

    private void Start()
    {
        if (cursorVisual) cursorVisual.SetActive(false);
    }

    public override void SetCursorStartDest(Vector3 start, Vector3 dest, Vector3 normal)
    {
        _startPoint = start;
        //_endPoint = dest;
        //_hitTarget = true;
    }

    public override void SetCursorRay(Transform t)
    {
        _startPoint = t.position;
        _forward = t.forward;
        //_hitTarget = false;
    }

    private void Update()
    {
        if (OVRInput.GetDown(OVRInput.Button.Two))
        {
            canMove = !canMove;
            lineRenderer.enabled = canMove;
        }
        if (!canMove) return;
        // Bit shift the index of the layer (8) to get a bit mask
        int layerMask = 1 << 4;

        // This would cast rays only against colliders in layer 8.
        // But instead we want to collide against everything except layer 8. The ~ operator does this, it inverts a bitmask.
        //layerMask = ~layerMask;

        RaycastHit hit;
        bool isHit = Physics.Raycast(_startPoint, _forward, out hit, maxLength, layerMask);
        Debug.DrawRay(_startPoint, _forward * 10, Color.yellow);
        _hitTarget = isHit;

        if (isHit) {
            // && hit.transform.gameObject.name == "ground"
            //Debug.DrawRay(_startPoint, _forward * hit.distance, Color.yellow);
            Debug.Log("Did Hit: " + hit.transform.gameObject.name);
            _endPoint = hit.point;
        }

        
    }

    private void LateUpdate()
    {
        if (!canMove) return;
        lineRenderer.SetPosition(0, _startPoint);
        if (_hitTarget)
        {
            lineRenderer.SetPosition(1, _endPoint);
            UpdateLaserBeam(_startPoint, _endPoint);
            if (cursorVisual)
            {
                cursorVisual.transform.position = _endPoint;
                cursorVisual.SetActive(true);
                if (canMove && OVRInput.GetDown(OVRInput.Button.One))
                {
                    cameraRig.position = new Vector3(_endPoint.x, cameraRig.position.y, _endPoint.z);
                    // StartCoroutine(Rest());
                }
            }
        }
        else
        {
            UpdateLaserBeam(_startPoint, _startPoint + maxLength * _forward);
            lineRenderer.SetPosition(1, _startPoint + maxLength * _forward);
            if (cursorVisual) cursorVisual.SetActive(false);
        }
    }

    // make laser beam a behavior with a prop that enables or disables
    private void UpdateLaserBeam(Vector3 start, Vector3 end)
    {
        if(laserBeamBehavior == LaserBeamBehavior.Off)
        {
            return;
        }
        else if(laserBeamBehavior == LaserBeamBehavior.On)
        {
            lineRenderer.SetPosition(0, start);
            lineRenderer.SetPosition(1, end);
        }
        else if(laserBeamBehavior == LaserBeamBehavior.OnWhenHitTarget)
        {
            if(_hitTarget)
            {
                if (!lineRenderer.enabled)
                {
                    lineRenderer.enabled = true;
                    lineRenderer.SetPosition(0, start);
                    lineRenderer.SetPosition(1, end);
                }
            }
            else
            {
                if(lineRenderer.enabled)
                {
                    lineRenderer.enabled = false;
                }
            }
        }
    }

    void OnDisable()
    {
        if(cursorVisual) cursorVisual.SetActive(false);
    }

    IEnumerator Rest() {
        canMove = false;
        yield return new WaitForSeconds(1);
        canMove = true;
    }
}
