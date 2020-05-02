using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ArrowEffect : MonoBehaviour
{
    [SerializeField] float minY, maxY, moveTime;
    [SerializeField] RectTransform rec;
    [SerializeField] bool isMovingUp = false;
    float changeAmount;

    void Start()
    {
        rec = GetComponent<RectTransform>();
        changeAmount = (maxY - minY) / moveTime;
    }

    // Update is called once per frame
    void Update()
    {
        if (isMovingUp)
        {
            rec.anchoredPosition += new Vector2(0, changeAmount * Time.deltaTime);
            if (rec.anchoredPosition.y > maxY) {
                isMovingUp = false;
            }
        }
        else {
            rec.anchoredPosition -= new Vector2(0, changeAmount * Time.deltaTime);
            if (rec.anchoredPosition.y < minY)
            {
                isMovingUp = true;
            }
        }
    }


}
