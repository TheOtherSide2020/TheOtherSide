using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VRTouchPoint : MonoBehaviour
{
    TouchPoint tp;
    void Start()
    {
        tp = gameObject.GetComponent<TouchPoint>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Hand")) {

        }
    }

    private void OnTriggerStay(Collider other)
    {
        if (other.gameObject.CompareTag("Hand"))
        {

        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.gameObject.CompareTag("Hand"))
        {

        }
    }
}
