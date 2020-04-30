using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OptionPulseEffect : MonoBehaviour
{
    [SerializeField] float scaleMin, scaleMax;
    [SerializeField] bool activePulsing = false;
    [SerializeField] bool scaleUp = false;
    [SerializeField] float pulseUnitTime, changeAmount;
    private void Start()
    {
        changeAmount = (scaleMax - scaleMin) / pulseUnitTime;
        SetActive(true);
    }

    public void SetActive(bool isActive) {
        activePulsing = isActive;
    }

    // Update is called once per frame
    void Update()
    {
        if (activePulsing) {
            if (scaleUp)
            {
                transform.localScale += Time.deltaTime * new Vector3(changeAmount, changeAmount, changeAmount);
                if (transform.localScale.x >= scaleMax) {
                    scaleUp = false;
                }
            }
            else {
                transform.localScale -= Time.deltaTime * new Vector3(changeAmount, changeAmount, changeAmount);
                if (transform.localScale.x <= scaleMin)
                {
                    scaleUp = true;
                }
            }
        }
    }
}
