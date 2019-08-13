import React from 'react';
import Item from '../item/Item'
import Accordion from 'react-bootstrap/Accordion'
import './AccordionItems.css'

class AccordionItems extends React.Component {
    constructor(props) {

        super(props);

        this.state = {
            error: null,
            isLoaded: false,
            items: []
          };

    }

    componentDidMount() {
        fetch("http://localhost:5000/transactions")
          .then(res => res.json())
          .then(
            (result) => {
                console.log(result);
              this.setState({
                isLoaded: true,
                items: result
              });
            },
            (error) => {
              this.setState({
                isLoaded: true,
                error
              });
            }
          )
    }

    render() {

        const { error, isLoaded, items } = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div class="loading">Loading...</div>;
        } else if (items) {
            return (
                <Accordion>
                    <div class="card-header container">
                        <div class="row">
                            <div class="col-sm">Date</div>
                            <div class="col-sm">Description</div>
                            <div class="col-sm">Amount</div>
                        </div>
                    </div>
                    {items.map((item, key) =>
                        <Item item={item} key={item.id} />
                    )}
                </Accordion>

            );
        }
        return (<div></div>);
    }
}

export default AccordionItems;