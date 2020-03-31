using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 vec = OVRInput.Get(OVRInput.Axis2D.PrimaryThumbstick).normalized * 0.01f;
        //Debug.Log(vec);
        transform.position += new Vector3(vec.x, 0, vec.y);
    }
}
